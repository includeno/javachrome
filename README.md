# javachrome

OpenJdk and Selenium Environment

link to dockerhub

https://hub.docker.com/r/includeno/javachrome


## Linux Reading Json 例子

### 指令

echo '{"hostname":"test","domainname":"example.com"}' | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hostname"])'

### 文件

tail ./xxx.json | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hostname"])'

tail ./configx64.json | python -c 'import json,sys;obj=json.load(sys.stdin);print(str(obj["JdkVersion"]).replace(":", "-"))'

tail ./configx64.json | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["ChromeVersion"])'