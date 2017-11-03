import urllib2
import os

# get url and sha1

which_one = raw_input("please tell me which project you want to integate:" + "1 inst, 2 stud, 3 both")
sdk_version = raw_input("please input sdk version(eg. 3.2.2-dev-new.2): ")

base_url = "http://maven.bbpd.io/content/repositories/bb-mobile-sdk-ios/com/blackboard/mobile-sdk/ios/"

inst_sdk_url = base_url + "BBMobileSDK.Instructor/%s/BBMobileSDK.Instructor-%s.zip" % (sdk_version, sdk_version)
stud_sdk_url = base_url + "BBMobileSDK.Student/%s/BBMobileSDK.Student-%s.zip" % (sdk_version, sdk_version)

inst_sdk_sha1_url = inst_sdk_url + ".sha1"
stud_sdk_sha1_url = stud_sdk_url + ".sha1"

if int(which_one) == 1:
    inst_f = urllib2.urlopen(inst_sdk_sha1_url)
    inst_sha1 = inst_f.read()
    print inst_sdk_url
    print inst_sdk_sha1_url
    print inst_sha1
elif int(which_one) == 2:
    stud_f = urllib2.urlopen(stud_sdk_sha1_url)
    stud_sha1 = stud_f.read()
    print stud_sdk_url
    print stud_sdk_sha1_url
    print stud_sha1
else:
    inst_f = urllib2.urlopen(inst_sdk_sha1_url)
    stud_f = urllib2.urlopen(stud_sdk_sha1_url)
    inst_sha1 = inst_f.read()
    stud_sha1 = stud_f.read()
    print inst_sdk_url
    print stud_sdk_url
    print inst_sdk_sha1_url
    print stud_sdk_sha1_url
    print inst_sha1
    print stud_sha1

# post podspec

os.chdir("/Users/bchai/ios-bbspecs")

print os.getcwd()

def git_shell(git_command):
    try:
        return os.popen(git_command).read().strip()
    except:
        return None

if git_shell("git branch") != "master":
    git_shell("git checkout master")

git_shell("git pull")

if git_shell("git branch") != sdk_version:
    git_shell("git checkout -b " + sdk_version)

os.chdir("/Users/bchai/ios-bbspecs/BbStudentSDK")

fold_name = sdk_version[0:5] + sdk_version[13:]

try:
    os.mkdir(fold_name)
except OSError:
    pass

os.chdir("/Users/bchai/ios-bbspecs/BbStudentSDK/" + fold_name)

print os.getcwd()

if int(which_one) == 1:
    inst_spec_source = "  spec.source           = { :http => \"%s\", :sha1 => \"%s\"}\n" % (inst_sdk_url, inst_sha1)
    print inst_spec_source
elif int(which_one) == 2:
    stud_spec_source = "  spec.source           = { :http => \"%s\", :sha1 => \"%s\"}\n" % (stud_sdk_url, stud_sha1)
    print stud_spec_source

    stud_data = ""

    with open("BbStudentSDK.podspec", "r+") as f:
        for line in f.readlines():
            if line.find("spec.source") == 2:
                line = stud_spec_source
            stud_data += line
        f.close()

    with open("BbStudentSDK.podspec", "r+") as f:
        f.writelines(stud_data)
        print f.read()
        f.close()
else:
    inst_spec_source = "spec.source           = { :http => \"%s\", :sha1 => \"%s\"}\n" % (inst_sdk_url, inst_sha1)
    stud_spec_source = "spec.source           = { :http => \"%s\", :sha1 => \"%s\"}\n" % (stud_sdk_url, stud_sha1)
    print inst_spec_source
    print stud_spec_source