"""项目ID"""
project_Id = input("项目id：")

"""主机名"""
host_name = input("主机名：")

"""计费类型"""
while True:
    fee_Type = input("计费类型（按需：FEE_TYPE_NEED，包年/月填FEE_TYPE_MONTH_YEAR）：").upper()
    if fee_Type == "FEE_TYPE_NEED" or fee_Type == "FEE_TYPE_MONTH_YEAR":
        break
    else:
        print("请按要求填写！")

"""租期"""
if fee_Type == "FEE_TYPE_MONTH_YEAR":
    while True:
        cycle_count = int(input("租赁期限（1-12个月或者24个月或者36个月）："))
        if cycle_count >= 1 and cycle_count <= 12 or cycle_count == 24 or cycle_count == 36:
            break
        else:
            print("请按要求输入！")

"""子网ID"""
subnet_Id = input("子网id：")

"""安全组ID"""
security_Group_Id = input("安全组id：")

"""镜像ID"""
image_Id = input("镜像id：")

"""flavorID"""
flavor_Id = input("flavorid：")

"""磁盘类型"""
while True:
    sysDisk_Type = input("磁盘类型（HHD或者SSD）：").upper()  # 输入磁盘类型统一转为大写
    if sysDisk_Type == "HHD" or sysDisk_Type == "SSD":  # 判断磁盘类型
        break
    else:
        print("请按要求填写！")

"""磁盘大小"""
while True:
    disk_size = int (input("磁盘大小（GB）（20到200之间10的整数倍）："))  # 输入磁盘大小转为int类型
    if disk_size >=20 and disk_size <=200 and disk_size%10 == 0:  # 判断是否符合填写要求
        break
    else:
        print("请按要求填写！")

"""登录方式"""
while True:
    login_Type = input("登录方式（密码填PASSWORD, SSH密钥填SSHKEY）：").upper()  # 登录方式
    if login_Type == "PASSWORD" or login_Type == "SSHKEY":  # 判断登录方式是否符合要求
        break
    else:
        print("请按要求填写")

"""密码或者SSHID"""
if login_Type == "PASSWORD":  # 登录方式为密码需要设置密码
    while True:
        input_password = input("请设置密码(密码8-30位字符，需同时包含大小写、英文、数字，"
                               "不能为键盘上连续3位及以上字符，不可包含空格及以下字符# $ % & * < >)：")
        re_input_password = input("确认密码:")
        if input_password == re_input_password :
            passwd = re_input_password
            break
        else:
            print("两次密码不匹配，请重新输入")
else:
    input_sshKey_Id = input("请输入SSH密钥id：")
    passwd = None

"""区域地址"""
while True:
    url = input("请输入区域服务地址（cn-east-1.api.yovole.com，cn-north-1.api.yovole.com，cn-south-2.api.yovole.com）：")
    if url == "cn-east-1.api.yovole.com" or url == "cn-south-2.api.yovole.com" or url == "cn-north-1.api.yovole.com":
        break
    else:
        print("请按要求填写")

"""
POST https://cn-east-1.api.yovole.com/v1/vm/create
    x-ycs-timestamp: 2021-02-19T14:24:35:25Z
    x-ycs-requestid:
    x-ycs-security-authorization: Authorization:
"""

"""接口参数:"""
info = {
"projectId":project_Id,
"name":host_name,
"feeType":fee_Type,  # 按需填FEE_TYPE_NEED，包年/月填FEE_TYPE_MONTH_YEAR
"subnetId":subnet_Id,
"securityGroupId":security_Group_Id,
"imageId":image_Id,
"flavorId":flavor_Id,
"sysDiskType":sysDisk_Type,  # HHD或者SSD
"sysDiskCapacity": disk_size,  #单位为GB，需是10的整数倍，大小区间（20，200）
"loginType":login_Type,  # 密码: PASSWORD, SSH密钥: SSHKEY
"password":passwd,  # 登录方式设置的是密码必须填写
"cycleCount":cycle_count,  # 计费类型是包年/月必须填
"URL":url
}
print(info.values())