"""浙江大学"""

name = "ZOJ"

problem_url = "http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=%d"

encoding = "utf8"

minid = 1000

maxid = 10000

regexp = {
    "title": r'<span class="bigProblemTitle">(.+?)</span>',
    "timelimit": r'<font color="green">Time Limit: </font> (\d+?) Seconds',
    "memorylimit": r'<font color="green">Memory Limit: </font> (\d+?) KB',
    "description": r'</center>[\s\S]*?<hr>[\s\S]*?<p>([\s\S]+?)</p>',
    "input": r'<b>Input</b><br>[\s\S]*?<br>([\s\S]+?)</p>',
    "output": r'<h4>Output</h4>[\s\S]*?<div class="prob-content">([.\s\S]+?)</div>[\s\S]*?<h4>Sample Input',
    "sampleinput": r'<b>Sample Input</b><br>[\s\S]*?<br>([\s\S]+?)<p><br>',
    "sampleoutput": r'<b>Sample Output</b><br>[\s\S]*?<br>([\s\S]+?)</p>',
    "source": r'Source: <strong>([\s\S]+?)</strong><br>',
}

def replace_src(description):
    return description.replace(r"src=", r"src=http://acm.zju.edu.cn/")
