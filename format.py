import requests
import re
import os

def getVersions():
    url="http://npm.taobao.org/mirrors/chromedriver"

    res = requests.get(url)
    html_origin = res.text

    versions = re.search('(\d){2,3}\.(\d)+\.(\d+)+', html_origin)
    print(versions)
    versions=re.findall(r'\d{2,3}\.\d+\.\d+\.\d+',html_origin)
    myset=set()
    for item in versions:
        myset.add(item)
        print(item)
    return list(myset)
#比较版本号
def compareVersion(version1: str, version2: str) -> int:
    nums1 = version1.split('.')
    nums2 = version2.split('.')
    n1, n2 = len(nums1), len(nums2)
    
    # compare versions
    for i in range(max(n1, n2)):
        i1 = int(nums1[i]) if i < n1 else 0
        i2 = int(nums2[i]) if i < n2 else 0
        if i1 != i2:
            return 1 if i1 > i2 else -1
    
    # the versions are equal
    return 0 

if __name__ == '__main__':
    versions=getVersions()
    versions.sort()
    #VersionBYRequests
    latest=versions[-1]

    filename="config"
    #config文件
    outfile = open(filename, "r", encoding='utf-8')
    lines=outfile.readlines()
    outfile.close()

    outfile = open(filename, "w", encoding='utf-8')
    for line in lines:
        outfile.write(line.replace(":","-").replace("VersionBYRequests",latest))
    outfile.close()