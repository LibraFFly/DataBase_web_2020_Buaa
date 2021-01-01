from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import datetime

from users.models import All_Users
from web_db.base import check_login
from web_for_dbwork2.models import Course_Info, Course_Major, Major_In_System, Study_Field, Teacher_Course, \
    Teacher_Info, Resource_Web, Resource_Book, Recommend_Item_Major, Course_Sequence, Recommend_Item_Route, \
    Recommend_Item, Broadcast_Record, Favorite_Record, Grade_Num, Campus_Life

from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@check_login
def index(request):
    # is_login = request.session.get('is_login')
    # if is_login:
    #     return redirect('web_for_dbwork2:index')

    # 这里将来自数据库的的数据放到一个变量中，然后可以在html中显示
    test_list = ["张", "李"]
    context = {'test_list': test_list}
    return render(request, 'web_for_dbwork2/index.html', context)


# 专业
@check_login
def major_c2m(request):
    res = {}
    if request.method == "POST":
        search_course = request.POST.get("search_course")
        if search_course == "":
            return redirect("web_for_dbwork2:major_c2m")
        print(search_course)

        course_info = Course_Info.objects.filter(course_name=search_course).values("course_id")
        course_id = course_info[0]["course_id"]

        # 一门课程对应多个专业
        major_id_list = []
        course_major = Course_Major.objects.filter(course_id=course_id).values("major_id")
        for i in course_major:
            major_id_list.append(i["major_id"])

        major_name_list = []

        for i in major_id_list:
            major_in_sys = Major_In_System.objects.filter(major_id=i).values("major_name")
            major_name = major_in_sys[0]["major_name"]
            major_name_list.append(major_name)

        ############################################################################################################
        # 待定，研究方向需不需要

        # 专业id对应专业研究方向表  的  字典
        # dict_filed = {}
        field_list_list = []
        field_desc_list_list = []
        for i in major_id_list:
            study_filed_list = Study_Field.objects.filter(major_id=i)
            # dict_filed[i] = study_filed_list
            list = []
            list_desc = []
            for j in study_filed_list:
                list.append(j.study_field_name)
                list_desc.append(j.study_field_desc)
            field_list_list.append(list)
            field_desc_list_list.append(list_desc)

        # 研究方向 专业名-研究方向名
        field_dict = {}
        i = -1
        for name in major_name_list:
            i = i + 1
            field_dict[name] = field_list_list[i]

        # 给每个研究方向名对应一个研究描述，放进字典
        i = -1
        j = -1
        desc = {}
        for field_list in field_list_list:
            i = i + 1
            j = -1
            for field in field_list:
                j = j + 1
                desc[field] = field_desc_list_list[i][j]

        res = {'name_list': major_name_list, 'field_dict': field_dict, 'desc': desc, 'has_data': 1}

        return render(request, "web_for_dbwork2/major_c2m.html", res)

    return render(request, "web_for_dbwork2/major_c2m.html")


@check_login
def major_m2c(request):
    if request.method == "POST":

        res = {}

        search_major = request.POST.get("search_major")

        if search_major == "":
            return redirect("web_for_dbwork2:major_m2c")
        # 取major_id
        major_id = Major_In_System.objects.filter(major_name=search_major).values("major_id")[0]['major_id']

        # 取多个course_id
        course_id_list = []
        course_ids = Course_Major.objects.filter(major_id=major_id).values("course_id")
        for i in course_ids:
            course_id_list.append(i['course_id'])

        # 拿具体课程信息
        list = []
        for course_id in course_id_list:
            course_info = Course_Info.objects.filter(course_id=course_id)

            # 拿教师具体信息
            teacher_id_dict = Teacher_Course.objects.filter(course_id=course_id).values("teacher_id")
            teacher_info_list = []
            for i in teacher_id_dict:
                teacher_id = i["teacher_id"]
                teacher_info = Teacher_Info.objects.filter(teacher_id=teacher_id)

                teacher_info_list.append({'name': teacher_info[0].teacher_name,
                                          'age': teacher_info[0].teacher_age,
                                          'rank': teacher_info[0].teacher_rank})

            # 拿网页资源
            web_resource_list = []
            web_resource = Resource_Web.objects.filter(course_id=course_id)
            for i in web_resource:
                web_resource_list.append({'ISBN': i.resource_ISBN, 'name': i.resource_name})

            # 拿书籍资源
            book_resource_list = []
            book_resource = Resource_Book.objects.filter(course_id=course_id)
            for i in book_resource:
                book_resource_list.append({'ISBN': i.resource_ISBN, 'name': i.resource_name})

            list.append({'course_name': course_info[0].course_name,
                         'recommend_learn_grade': course_info[0].recommend_learn_grade,
                         'credits': course_info[0].credits,
                         'avg_grades': course_info[0].avg_grades,
                         'teacher_info_list': teacher_info_list,
                         'web_resource_list': web_resource_list,
                         'book_resource_list': book_resource_list})

        res['course_info'] = list

        res['major_name'] = search_major
        res['has_data'] = 1


        # 拿研究方向
        field_name = Study_Field.objects.filter(major_id=major_id)
        field = []
        for name in field_name:
            field.append(name.study_field_name)
        res['study_field'] = field

        return render(request, 'web_for_dbwork2/major_m2c.html', res)

    return render(request, 'web_for_dbwork2/major_m2c.html')


@check_login
def major_recommend(request):
    xinxi_1 = 1
    xinxi_2 = 7
    hang_1 = 8
    hang_2 = 12
    like_1 = 13
    like_2 = 16
    wenke_1 = 17
    wenke_2 = 21
    res = {}

    major_cate = {'xx': {}, 'hkht': {}, 'lk': {}, 'wk': {}}
    major_id_name = Major_In_System.objects.all()
    for i in range(1, wenke_2 + 1):
        if i <= xinxi_2:
            major_cate['xx'][str(i)] = major_id_name[i - 1].major_name
        elif hang_1 <= i <= hang_2:
            major_cate['hkht'][str(i)] = major_id_name[i - 1].major_name
        elif like_1 <= i <= like_2:
            major_cate['lk'][str(i)] = major_id_name[i - 1].major_name
        elif wenke_1 <= i <= wenke_2:
            major_cate['wk'][str(i)] = major_id_name[i - 1].major_name

    res['cate'] = major_cate
    if request.method == "POST":
        # 取到选择的id
        major_id = 1
        for major_id_choose in range(1, wenke_2 + 1):
            if_choose = request.POST.get(str(major_id_choose))
            major_id = int(major_id_choose)
            print(if_choose)
            if if_choose == "on":
                break

        # 拿到major_name
        major_name = Major_In_System.objects.filter(major_id=major_id).values("major_name")[0]["major_name"]

        # 通过major_name去拿专业推荐各种信息
        recommend_major_info = Recommend_Item_Major.objects.filter(major_name=major_name)
        info_list = []
        for one in recommend_major_info:
            title = one.major_title
            desc = one.major_desc
            rep1 = one.major_representive_course_1
            rep2 = one.major_representive_course_2
            rep3 = one.major_representive_course_3
            # 转换成名字
            rep1 = Course_Info.objects.filter(course_id=rep1)[0].course_name
            rep2 = Course_Info.objects.filter(course_id=rep2)[0].course_name
            rep3 = Course_Info.objects.filter(course_id=rep3)[0].course_name

            label1 = one.major_label_1
            label2 = one.major_label_2
            label3 = one.major_label_3
            like_num = one.like_num
            hot = one.hot
            watch = one.watch
            info_list.append({'title': title, 'desc': desc, 'rep1': rep1, 'rep2': rep2, 'rep3': rep3,
                              'label1': label1, 'label2': label2,
                              'label3': label3, 'like_num': like_num, 'hot': hot, 'watch': watch})

        res['recommend_info'] = info_list
        res['major_name'] = major_name
        print(major_name)

    return render(request, 'web_for_dbwork2/major_recommend.html', res)


# 学习
@check_login
def study_main(request):
    res = {'name': "hujinfei"}

    if request.method == "POST":
        search_course = request.POST.get("search_course")
        if search_course == "":
            return redirect("web_for_dbwork2:study_main")
        course_id = Course_Info.objects.filter(course_name=search_course)[0].course_id

        # 取多个route_id
        routes = Course_Sequence.objects.filter(course_id=course_id).values("route_id")
        route_list = []

        # 记录一下热度最大的下标
        maxHot = -1
        index = 0
        i = -1

        for one in routes:
            i = i + 1
            route_id = one["route_id"]
            rec_route = Recommend_Item_Route.objects.filter(item_route_id=route_id)
            route_name = rec_route[0].route_name
            item_id = rec_route[0].item_id
            like_num = rec_route[0].like_num
            hot = rec_route[0].hot
            if hot > maxHot:
                maxHot = hot
                index = i
            watch = rec_route[0].watch

            # 取user_id
            user_id = Recommend_Item.objects.filter(item_id=item_id)[0].user_id
            user_name = All_Users.objects.filter(user_id=user_id)[0].user_name

            route_list.append({'route_name': route_name, 'hot': hot, 'watch': watch, 'like_num': like_num,
                               'route_id': route_id, 'user_name': user_name})

        # 热度最大的提出来
        temp = route_list[index]
        route_list.pop(index)

        res['hot_route'] = temp
        res['route_list'] = route_list
        res['has_data'] = 1

    return render(request, 'web_for_dbwork2/study_main.html', res)


@check_login
def study_router(request):
    res = {}
    route_id = request.GET.get('route_id')
    res['route_id'] = route_id

    rec_item_route = Recommend_Item_Route.objects.filter(item_route_id=route_id)
    watch = rec_item_route[0].watch + 1
    like_num = rec_item_route[0].like_num
    hot = like_num * like_num * watch + like_num + watch
    Recommend_Item_Route.objects.filter(item_route_id=route_id).update(watch=watch, hot=hot)

    # 取所有在该路线上的课程
    route_course = Course_Sequence.objects.filter(route_id=route_id)
    course_list = []

    # 路径顺序从1开始计数
    course_list.append(0)
    for course in route_course:
        course_list.append(0)
    for course in route_course:
        course_list[course.sequence_number] = course.course_id

    # 现在还只是按顺序的id
    course_list = course_list[1:]

    # 取具体课程信息
    course_info_list = []
    for course_id in course_list:
        course_info = Course_Info.objects.filter(course_id=course_id)
        course_info_list.append({'name': course_info[0].course_name,
                                 'recommend_learn_grade': course_info[0].recommend_learn_grade,
                                 'credits': course_info[0].credits, 'avg_grades': course_info[0].avg_grades})

    res['course_info_list'] = course_info_list

    route_name = Recommend_Item_Route.objects.filter(item_route_id=route_id)[0].route_name
    res['route_name'] = route_name

    return render(request, 'web_for_dbwork2/study_router.html', res)


# 生活
@check_login
def life(request):
    data = Campus_Life.objects.all()
    list = []
    for i in data:
        content = i.content
        temp = content.split("-")
        list.append({'title': i.recommend_title, 'content': temp[1], 'label': temp[0]})
    res = {'life_list': list}
    return render(request, 'web_for_dbwork2/life.html', res)


# 添加帖子

# 生活帖子
def add_life_topic(request):
    return render(request, 'web_for_dbwork2/add_life_topic.html')


# 专业推荐帖子
def add_major_recommend(request):
    if request.method == "POST":
        major_name = request.POST.get("major_name")
        major_desc = request.POST.get("major_desc")
        major_title = request.POST.get("major_title")
        major_rep1 = request.POST.get("major_rep1")
        major_rep2 = request.POST.get("major_rep2")
        major_rep3 = request.POST.get("major_rep3")
        major_l1 = request.POST.get("major_label1")
        major_l2 = request.POST.get("major_label2")
        major_l3 = request.POST.get("major_label3")

        rep1 = Course_Info.objects.filter(course_name=major_rep1)[0].course_id
        rep2 = Course_Info.objects.filter(course_name=major_rep2)[0].course_id
        rep3 = Course_Info.objects.filter(course_name=major_rep3)[0].course_id

        ins = Recommend_Item(user_id=request.COOKIES.get('user_id'), item_name=major_title, total_hot=0)
        ins.save()
        item_id = Recommend_Item.objects.last().item_id

        ins = Recommend_Item_Major(item_id=item_id, major_name=major_name, major_desc=major_desc,
                                   major_title=major_title, major_representive_course_1=rep1,
                                   major_representive_course_2=rep2, major_representive_course_3=rep3,
                                   major_label_1=major_l1, major_label_2=major_l2, major_label_3=major_l3,
                                   like_num=0, watch=0, hot=0
                                   )
        ins.save()

        ins = Broadcast_Record(user_id=request.COOKIES.get('user_id'),
                               broadcast_time=datetime.date.today(), title=major_title)
        ins.save()

        return redirect("web_for_dbwork2:major_recommend")
    return render(request, 'web_for_dbwork2/add_major_recommend.html')


# 学习路线添加
def add_study_router(request):
    if request.method == "POST":
        route_title = request.POST.get("router_title")
        route_text = request.POST.get("router_text")
        # rec_item
        ins = Recommend_Item(user_id=request.COOKIES.get('user_id'), item_name=route_title, total_hot=0)
        ins.save()
        item_id = Recommend_Item.objects.last().item_id

        # rec_item_route
        ins = Recommend_Item_Route(item_id=item_id, route_name=route_title, like_num=0, watch=0, hot=0)
        ins.save()

        route_id = Recommend_Item_Route.objects.last().item_route_id

        # 需要得到添加的路线上的课程id
        course_name_list = route_text.split('-')
        course_id_list = []
        for name in course_name_list:
            id = Course_Info.objects.filter(course_name=name)[0].course_id
            course_id_list.append(id)

        # 开始添加course_sequence
        i = 0
        for id in course_id_list:
            i = i + 1
            ins = Course_Sequence(route_id=route_id, course_id=id, sequence_number=i)
            ins.save()

        # 用户发布记录
        ins = Broadcast_Record(user_id=request.COOKIES.get('user_id'),
                               broadcast_time=datetime.date.today(), title=route_title)
        ins.save()

        return redirect("web_for_dbwork2:study_main")
    return render(request, 'web_for_dbwork2/add_study_router.html')


def add_xing(request):
    route_id = request.GET.get("route_id")
    rec_item_route = Recommend_Item_Route.objects.filter(item_route_id=route_id)
    route_name = rec_item_route[0].route_name
    user_id = request.COOKIES.get("user_id")
    temp_ins = Favorite_Record.objects.filter(favorite_title=route_name, user_id=user_id)

    if len(temp_ins) != 0:
        messages.warning(request, "您已收藏过该推荐贴，请查看")
        return redirect("users:person_information")


    like_num = rec_item_route[0].like_num + 1
    watch = rec_item_route[0].watch
    hot = like_num * like_num * watch + like_num + watch
    Recommend_Item_Route.objects.filter(item_route_id=route_id).update(like_num=like_num, hot=hot)

    item_id = rec_item_route[0].item_id
    owner_id = Recommend_Item.objects.filter(item_id=item_id)[0].user_id
    owner_name = All_Users.objects.filter(user_id=owner_id)[0].user_name


    fav_time = datetime.date.today()
    ins = Favorite_Record(user_id=user_id, favorite_time=fav_time, favorite_title=route_name,
                          favorite_content_id="study-" + str(route_id), owner_name=owner_name)

    ins.save()
    messages.success(request, "收藏成功，现在您可以查看您收藏的帖子")
    return redirect("users:person_information")


def add_grade(request):
    grade = request.POST.get("grade")
    name = request.POST.get("name")
    course_id = Course_Info.objects.filter(course_name=name)[0].course_id
    ins = Grade_Num.objects.filter(id=course_id)
    if len(ins) == 0:
        ins1 = Grade_Num(id=course_id, num=0)
        ins1.save()

    num = Grade_Num.objects.filter(id=course_id)[0].num
    avg = Course_Info.objects.filter(course_name=name)[0].avg_grades

    f = float(avg)
    sum = num * f
    sum = sum + (float(grade))
    num = num + 1
    Grade_Num.objects.filter(id=course_id).update(num=num)
    f = sum / num
    Course_Info.objects.filter(course_name=name).update(avg_grades=str(f))
    return redirect("web_for_dbwork2:major_m2c")


def add_life(request):
    title = request.POST.get("title")
    label = request.POST.get("label")
    text = request.POST.get("text")
    user_id = request.COOKIES.get('user_id')
    ins = Recommend_Item(user_id=user_id, item_name=title, total_hot=0)
    ins.save()

    item_id = Recommend_Item.objects.last().item_id
    ins = Campus_Life(item_id=item_id, recommend_title=title, content=label + "-" + text, author_id=user_id,
                      created_time=datetime.date.today(), like_num=0, watch=0, hot=0)
    ins.save()
    return redirect("web_for_dbwork2:life")



#  测试用
@check_login
def page1(request):
    text_list = ["hello", "word"]
    contex = {'text_list': text_list}
    return render(request, 'web_for_dbwork2/page1.html', contex)


@check_login
def page2(request):
    # 获取当前时间
    now = datetime.datetime.now()
    return render(request, 'web_for_dbwork2/page2.html', {"time_now": now})
