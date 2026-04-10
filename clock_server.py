from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>实时钟表</title>
<style>
body {
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:#eef2f7;
}
.clock {
    position:relative;
    width:300px;
    height:300px;
    border:10px solid #222;
    border-radius:50%;
    background:white;
}
.hand {
    position:absolute;
    bottom:50%;
    left:50%;
    transform-origin:bottom;
    transform:translateX(-50%) rotate(0deg);
}
.hour { width:6px; height:70px; background:#111; }
.minute { width:4px; height:100px; background:#333; }
.second { width:2px; height:120px; background:red; }
.center {
    position:absolute;
    top:50%; left:50%;
    width:12px; height:12px;
    background:#111;
    border-radius:50%;
    transform:translate(-50%,-50%);
}
</style>
</head>

<body>

<div class="clock">
    <div class="hand hour" id="h"></div>
    <div class="hand minute" id="m"></div>
    <div class="hand second" id="s"></div>
    <div class="center"></div>
</div>

<script>
function update(){
    const n=new Date();

    let h=n.getHours()%12;
    let m=n.getMinutes();
    let s=n.getSeconds();

    document.getElementById("h").style.transform =
        `translateX(-50%) rotate(${h*30+m*0.5}deg)`;

    document.getElementById("m").style.transform =
        `translateX(-50%) rotate(${m*6}deg)`;

    document.getElementById("s").style.transform =
        `translateX(-50%) rotate(${s*6}deg)`;
}

setInterval(update,1000);
update();
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)