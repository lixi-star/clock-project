from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>实时钟表</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: #eef2f7;
            font-family: Arial, "Microsoft YaHei", sans-serif;
        }

        .clock {
            position: relative;
            width: 320px;
            height: 320px;
            border: 10px solid #222;
            border-radius: 50%;
            background: #ffffff;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        }

        .ticks, .numbers {
            position: absolute;
            width: 100%;
            height: 100%;
            left: 0;
            top: 0;
        }

        /* 小刻度 */
        .tick {
            position: absolute;
            left: 50%;
            top: 50%;
            width: 2px;
            height: 10px;
            background: #666;
            transform-origin: center 132px;
        }

        /* 大刻度：缩短并向内移，避免挡住数字 */
        .tick.major {
            width: 4px;
            height: 12px;
            background: #222;
            transform-origin: center 130px;
        }

        /* 数字 */
        .numbers span {
            position: absolute;
            font-size: 24px;
            font-weight: bold;
            color: #222;
            transform: translate(-50%, -50%);
            user-select: none;
        }

        /* 指针 */
        .hand {
            position: absolute;
            bottom: 50%;
            left: 50%;
            transform-origin: bottom center;
            transform: translateX(-50%) rotate(0deg);
            border-radius: 10px;
        }

        .hour {
            width: 8px;
            height: 75px;
            background: #111;
            z-index: 5;
        }

        .minute {
            width: 5px;
            height: 105px;
            background: #333;
            z-index: 6;
        }

        .second {
            width: 2px;
            height: 125px;
            background: red;
            z-index: 7;
        }

        .center {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 14px;
            height: 14px;
            background: #111;
            border-radius: 50%;
            transform: translate(-50%, -50%);
            z-index: 8;
        }

        .center::after {
            content: "";
            position: absolute;
            width: 6px;
            height: 6px;
            background: #fff;
            border-radius: 50%;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
    </style>
</head>
<body>

<div class="clock">
    <div class="ticks" id="ticks"></div>
    <div class="numbers" id="numbers"></div>

    <div class="hand hour" id="h"></div>
    <div class="hand minute" id="m"></div>
    <div class="hand second" id="s"></div>
    <div class="center"></div>
</div>

<script>
    // ========= 生成刻度 =========
    const ticks = document.getElementById("ticks");

    for (let i = 0; i < 60; i++) {
        const tick = document.createElement("div");
        tick.className = "tick";
        if (i % 5 === 0) {
            tick.classList.add("major");
        }

        tick.style.transform = `translate(-50%, -132px) rotate(${i * 6}deg)`;
        ticks.appendChild(tick);
    }

    // ========= 生成数字 1~12 =========
    const numbers = document.getElementById("numbers");
    const centerX = 160;
    const centerY = 160;
    const radius = 111;

    for (let i = 1; i <= 12; i++) {
        const span = document.createElement("span");
        span.innerText = i;

        const angle = (i * 30 - 90) * Math.PI / 180;
        const x = centerX + radius * Math.cos(angle);
        const y = centerY + radius * Math.sin(angle);

        span.style.left = x + "px";
        span.style.top = y + "px";

        numbers.appendChild(span);
    }

    // ========= 更新时间 =========
    function updateClock() {
        const n = new Date();

        const h = n.getHours() % 12;
        const m = n.getMinutes();
        const s = n.getSeconds();

        const hourDeg = h * 30 + m * 0.5;
        const minuteDeg = m * 6 + s * 0.1;
        const secondDeg = s * 6;

        document.getElementById("h").style.transform =
            `translateX(-50%) rotate(${hourDeg}deg)`;

        document.getElementById("m").style.transform =
            `translateX(-50%) rotate(${minuteDeg}deg)`;

        document.getElementById("s").style.transform =
            `translateX(-50%) rotate(${secondDeg}deg)`;
    }

    setInterval(updateClock, 1000);
    updateClock();
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