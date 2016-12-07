# coding=utf-8

from PIL import Image, ImageDraw, ImageFont
import random
import os, platform

if platform.system() == "Windows":
    fontType = os.path.dirname(os.path.abspath(__file__)) + "\\Gabriola.ttf"
else:
    fontType = os.path.dirname(os.path.abspath(__file__)) + "/Gabriola.ttf"


def gener_image():
    letters = random.sample('adcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ234567890', 5)
    width = 400
    height = 200
    im = Image.new("RGB", (width, height))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(fontType, 50)
    for i in range(4):
        dr.text((5 + i * 20, 5), letters[i], (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                font)
    del dr

    for x in range(width):
        for y in range(height):
            if im.getpixel((x, y)) == (255, 255, 255):
                im.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    import base64
    from io import BytesIO
    out = BytesIO()
    im.save(out, "PNG")
    imgstr = base64.b64encode(out.getvalue()).decode('ascii')
    imgstr.save("xxx.png")
    # img_tag = '<img src="data:image/png;base64,{0}">'.format(imgstr)
    return imgstr
    dict()


if __name__ == '__main__':
    # print os.path.dirname(os.path.abspath(__file__))
    # gener_image()
    allfunc = {
        "ContentMod#details" : "文章详情",
        "CommentMod#get_list" : "获取评论",
        "PermissionMod#setup_model" : "维护权限模板",
        "CommentMod#remove" : "删除评论",
        "UserMod#modify" : "修改用户",
        "CommentMod#modify" : "修改评论",
        "UserMod#reset_pwd" : "重置密码",
        "CommentMod#add" : "添加评论",
        "CommentMod#details" : "评论详情",
        "ContentMod#get_list" : "查找文章",
        "ContentMod#insert" : "新增文章",
        "PushMod#push" : "推送通知",
        "PermissionMod#revoke" : "反授权",
        "ContentMod#review" : "文章审核",
        "PermissionMod#details" : "权限详情",
        "PermissionMod#remove_model" : "删除权限模板",
        "UserMod#create" : "创建用户",
        "UserMod#details" : "用户详情",
        "CommentMod#review" : "评论审核",
        "PermissionMod#get_list" : "用户权限列表",
        "ContentMod#remove" : "删除文章",
        "PermissionMod#grant" : "用户授权",
        "PushMod#get_list" : "推送列表",
        "UserMod#get_list" : "用户列表",
        "ContentMod#modify" : "修改文章"
    }
    for i in allfunc.keys():
        if "remove" in i:
            print i
    pass
