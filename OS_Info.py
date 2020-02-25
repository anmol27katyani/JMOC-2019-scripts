import math
import subprocess
from fpdf import FPDF as pdf

def decoder(byte_obj):
    return byte_obj.decode("utf-8").strip()

def ping_test():
    process = subprocess.Popen(["ping", "-c", "4", "8.8.8.8"],\
         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = process.communicate()
    for line in res:
        line = line.decode("utf-8")
        if "packet loss" in line:
            loss = int(line.split(",")[2].split("%")[0])
            if loss != 100:
                return True
    return False

def public_ip_get():
    process = subprocess.Popen(["dig", "+short", "myip.opendns.com", "@resolver1.opendns.com"], \
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = process.communicate()
    res = res[0].decode("utf-8").split("\n")
    return res[0]

def kernel_version():
    process = subprocess.Popen(["uname", "-r"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = process.communicate()
    res = res[0].decode("utf-8").split("\n")
    return res[0]

def java_version_checker():
    try:
        process = subprocess.Popen(["java", "-version"], \
           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        res = process.communicate()
    except:
        return "False"
    for line in res:
        line = line.decode("utf-8")
        if "version" in line:
            return line.split('\"')[1].split("_")[0]

def cpu_info():
    cpu_info_list = []
    param = ['Architecture', 'CPU op-mode', 'Model name']
    process = subprocess.Popen("lscpu", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = process.communicate()
    res = res[0].decode("utf-8").split("\n")
    for line in res:
        for each_param in param:
            if each_param in line:
                cpu_info_list.append(line.strip())
                continue
    return cpu_info_list

def pdf_info():
    #Result Variables
    internet_flag = ping_test()
    public_ip = ""
    kernel_ver = kernel_version()
    java_version = java_version_checker()
    cpu_info_list = cpu_info()

    pdf_doc = pdf()
    pdf_doc.add_page()
    pdf_doc.set_text_color(0, 0, 255)
    pdf_doc.set_font('Arial', 'B', 12) 
    pdf_doc.write(1.3, 'Linux System Information\n')
    pdf_doc.line(8, pdf_doc.get_y()+5, pdf_doc.w-5, pdf_doc.get_y()+5)
    pdf_doc.set_x(0)
    pdf_doc.set_y(pdf_doc.get_y()+7)
    pdf_doc.set_font('Arial', '', 10)
    pdf_doc.set_text_color(0, 0, 0)
    pdf_doc.write(5, 'This has the Information regarding the Linux')
    pdf_doc.write(5, ' System currently on which the script execute\n')
    pdf_doc.set_text_color(0, 0, 255)
    pdf_doc.write(5, 'Internet Connectivity\n')
    pdf_doc.set_text_color(0, 0, 0)
    if internet_flag:
        pdf_doc.write(5, 'Internet is Reachable. No Connectivity issue with internet\n')
        public_ip = public_ip_get()
    else:
        pdf_doc.write(5, 'Internet is not Reachable. Connectivity issues.')
        pdf_doc.write(5, 'Please check cables and relevant drivers\n')
    pdf_doc.set_text_color(0, 0, 255)
    pdf_doc.write(5, 'System Public IP\n')
    pdf_doc.set_text_color(0, 0, 0)
    if internet_flag:
        pdf_doc.write(5, 'Public IP of the System at current time is ' + public_ip + "\n")
    else:
        pdf_doc.write(5, 'Internet is not Reachable. Connectivity issues. So No Public IP\n')
    pdf_doc.set_text_color(0, 0, 255)
    pdf_doc.write(5, 'Kernel Version\n')
    pdf_doc.set_text_color(0, 0, 0)
    pdf_doc.write(5, 'The Kernel version of the system is '+ kernel_ver + '\n')
    pdf_doc.set_text_color(0, 0, 255)
    pdf_doc.write(5, 'Java Version\n')
    pdf_doc.set_text_color(0, 0, 0)
    if java_version == 'False':
        pdf_doc.write(5, 'Java Does Not exist in your system. Please install it\n')
    else:
        pdf_doc.write(5, 'The Java version of the system is '+ java_version + ' \n')
    pdf_doc.set_text_color(0, 0, 255)
    pdf_doc.write(5, 'CPU Information\n')
    pdf_doc.set_text_color(0, 0, 0)
    for item in cpu_info_list:
        pdf_doc.write(5, item + "\n")
    pdf_doc.output("Linux_System_Info.pdf")

pdf_info()
