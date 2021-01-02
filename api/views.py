from django.http import HttpResponse, JsonResponse

REPO = ["path_to_repo_1","path_to_repo_2"]
try: from .repo_info import *
except ImportError as e: pass

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
            dir_list.remove(".git")
            # 只保留 .md 文件
            for file_name in file_list:
                if file_name[-3:-1] != ".md":
                    file_list.remove(file_name)
                    
            result = {
                "dir_list":dir_list,
                "passage_list":file_list
            }
    print(result)
    
    return JsonResponse({})