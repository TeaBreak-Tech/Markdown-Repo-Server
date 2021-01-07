from django.http import HttpResponse, JsonResponse

#REPO = ["path_to_repo_1","path_to_repo_2"]
#try: from .repo_info import *
#except ImportError as e: pass
REPO = ["/home/www/Blog"]

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def listContent(request):
    import os
    #import csv
    result = {}
    repo_path = REPO[0]
    target = request.GET.get("target","/")
    target_path = repo_path+target
    for path,dir_list,file_list in os.walk(target_path):
        
        if path==target_path:
            try:dir_list.remove(".git")
            except:pass
            # 只保留 .md 文件
            print(file_list)
            md_list = []
            for file_name in file_list:
                print(file_name)
                if file_name.split(".")[-1] =="md":
                    md_list.append(file_name)
                else: print (file_name[-3:])
            result = {
                "target":target,
                "dir_list":dir_list,
                "passage_list":md_list,
            }
    print(result)
    return JsonResponse(result)

def getPassage(request):
    repo_path = REPO[0]
    target = request.GET.get("target","/README.md")
    target_path = repo_path+target
    f = open(target_path)
    lines = f.read()
    print(lines)
    return JsonResponse({
        "target":target,
        "content":lines,
    })