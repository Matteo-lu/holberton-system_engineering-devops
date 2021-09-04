<h1 class="gap">0x04. Loops, conditions and parsing</h1><div class="gap" id="project-description">
<h2>Background Context</h2>
<p><a href="https://youtu.be/BC2neyc5GcI" target="_blank"><img alt="" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/b07e3333b1edfb9beed5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210904%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210904T211615Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=e64d93906c334792039ca60e7ecb4fc20b34d3d85003827efee111641a2dfc8c" style=""/></a></p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a 6mzdeyytpw9r1k0hbkfubq"="" href="/rltoken/XnVjFM8a1W4RfRu4TCPY-g" rltoken="" target="_blank" title="Loops sample" tkpmmkxbw4dgkxdkt51fza"="" zoh3mqvvhyo_itinhksv6q"="">Loops sample</a> </li>
<li><a href="/rltoken/IM0Gv6VPzwAmqzlJxETZkw" target="_blank" title="Variable assignment and arithmetic">Variable assignment and arithmetic</a> </li>
<li><a href="/rltoken/K3E6xI9-goDM-93vsjCpPA" target="_blank" title="Comparison operators">Comparison operators</a> </li>
<li><a href="/rltoken/0OZLLDT28KrRZdid-l6hwg" target="_blank" title="File test operators">File test operators</a> </li>
<li><a href="/rltoken/Dyrnap2UC-LrzrmCOJRx8A" target="_blank" title="Make your scripts portable">Make your scripts portable</a> </li>
</ul>
<p><strong>man or help</strong>:</p>
<ul>
<li><code>env</code></li>
<li><code>cut</code></li>
<li><code>for</code></li>
<li><code>while</code></li>
<li><code>until</code></li>
<li><code>if</code></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a href="/rltoken/GXTAfCK7jqnNboT4MNdPFg" target="_blank" title="explain to anyone">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>How to create SSH keys</li>
<li>What is the advantage of using  <code>#!/usr/bin/env bash</code> over <code>#!/bin/bash</code></li>
<li>How to use <code>while</code>, <code>until</code> and <code>for</code> loops</li>
<li>How to use <code>if</code>, <code>else</code>, <code>elif</code> and <code>case</code> condition statements</li>
<li>How to use the <code>cut</code> command</li>
<li>What are files and other comparison operators, and how to use them</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>You are not allowed to use <code>awk</code></li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.3-1~ubuntu14.04.1</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>
<h2>More Info</h2>
<h3>Shellcheck</h3>
<p><a href="/rltoken/E7Pr2zeM3cdY5-C0HKwtbw" target="_blank" title="Shellcheck">Shellcheck</a> is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. <code>Shellcheck</code> is your friend! <strong>All your Bash scripts must pass <code>Shellcheck</code> without any error or you will not get any points on the task</strong>.</p>
<p><code>Shellcheck</code> is available on the school’s computers. If you want to use it on your own computer, here is how to <a href="/rltoken/SOX0HZTMgzHbcxrvU1X4hw" target="_blank" title="install it">install it</a>.</p>
<p>Examples:</p>
<p>Not passing <code>Shellcheck</code>:<br/>
<br/>
<img alt="" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png" style=""/></p>
<p>Passing <code>Shellcheck</code>:<br/>
<br/>
<img alt="" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png" style=""/></p>
<p>For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code <code>SC2034</code>, you can browse <a href="/rltoken/1SeRQAUtYIpfXXIQeD1PFQ" target="_blank" title="https://github.com/koalaman/shellcheck/wiki/SC2034">https://github.com/koalaman/shellcheck/wiki/SC2034</a>.</p>
</div>actualization