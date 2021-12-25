jenkinFileBody = """
pipeline{
    agent any
    options {
        timeout(time: 1, unit: 'HOURS')  //指定一个小时的全局执行超时，之后Jenkins将中止Pipeline运行.
        quietPeriod(0) //修改流水线静默期 默认jenkins全局配置5秒
    }
    parameters {
        string defaultValue: '1', description: '环境', name: 'runenv', trim: true
        string defaultValue: 'ordercenter', description: '服务名称', name: 'appname', trim: true
        string defaultValue: 'ordercenter_v1.0.90_20210622_002_release-APPLET-149.tar.gz', description: '软件包名称', name: 'appversion', trim: true
        string defaultValue: 'release-APPLET-149#v1.0.90_20210622_002', description: '分支名称', name: 'branch', trim: true
        string defaultValue: '127.0.0.1', description: '实例ip地址', name: 'instance_ip', trim: true
        string defaultValue: '6', description: '项目地址', name: 'giturl', trim: true
        string defaultValue: '7', description: '语言类型', name: 'language_type', trim: true
        string defaultValue: '8', description: '发布类型VM/k8', name: 'release_type', trim: true
    }
    stages{
        stage('变量处理'){
            steps{
                script{
                  update_package = "/data/new/update/${appname}/Release"
                  tmp_package = "/tmp/update/${appname}/Release"
                  server_package_dir = "/xwkj/app/${appname}/dist/${branch}"
                  server_bin = "/xwkj/app/${appname}/bin"
                  server_dir = "/xwkj/app/${appname}"
                }
            }
        }
        stage('镜像CI阶段'){
            steps{
                script{
                //变量处理
                    server = server.split('/')[-1]
                    server = server.replaceAll("_", "-")
                    tmp = serverTag.split('/')[-1]
                    branch = tmp.split('#')[0]
                    version = tmp.split('#')[1]				
                    git branch: branch, changelog: false, credentialsId: voucherId, poll: false, url: gitUrl
					if ( language_type == 'java' ){
						sh("mvn -U  clean && mvn -U -Dmaven.test.skip=true  -q compile  package")
					}else if ( language_type == 'node' ){
					    sh("npm run install")
					}
				    sh("whoami")
					sh("docker build -t harbor.xxx.com/k8s/${language}/${server}:${version} .")
					sh("sudo docker push harbor.xxx.com/k8s/${language}/${server}:${version}")
					sh("sudo docker rmi harbor.xxx.com/k8s/${language}/${server}:${version}")
                }
            }
        }
    }
}
"""
