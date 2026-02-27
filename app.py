# app.py — REPLICA Event (Flask Web App)
# ---------------------------------------

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>REPLICA | Act as the Video Plays</title>

  <!-- AOS Scroll Animation -->
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">

  <!-- Google Font -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap" rel="stylesheet">

  <style>
    body{margin:0;font-family:Poppins;background:#0b0620;color:#fff}

    /* HERO SECTION */
    .hero{
      position:relative;
      height:100vh;
      background:linear-gradient(135deg,#1b0f3a,#090016);
      display:flex;
      justify-content:center;
      align-items:center;
      text-align:center;
      padding:20px;
    }

    h1{
      font-size:3.5rem;
      background:linear-gradient(90deg,#8a2be2,#00c3ff);
      -webkit-background-clip:text;
      -webkit-text-fill-color:transparent;
      font-weight:800;
    }

    h2{
      font-weight:300;
      margin:10px 0 20px;
    }

    .meta{
      display:flex;
      gap:15px;
      flex-wrap:wrap;
      justify-content:center;
      margin-top:20px;
    }

    .meta div{
      background:rgba(255,255,255,.1);
      padding:10px 18px;
      border-radius:12px;
    }

    .btn{
      margin-top:30px;
      padding:14px 36px;
      border:none;
      border-radius:40px;
      background:linear-gradient(90deg,#8a2be2,#00c3ff);
      font-weight:700;
      cursor:pointer;
      color:#fff;
    }

    section{padding:70px 8%}

    .grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
      gap:25px;
    }

    .card{
      background:rgba(255,255,255,.06);
      padding:30px;
      border-radius:18px;
      backdrop-filter:blur(8px);
    }

    /* COUNTDOWN */
    .countdown{
      display:flex;
      justify-content:center;
      gap:20px;
      margin-top:30px;
    }

    .time{
      background:#111;
      border-radius:14px;
      padding:18px;
      width:90px;
      text-align:center;
    }

    .time h3{
      margin:0;
      color:#00c3ff;
    }

    footer{
      text-align:center;
      padding:40px 20px;
      background:#050814;
    }

    footer h4{
      color:#8a2be2;
    }

    @media(max-width:600px){
      h1{font-size:2.2rem}
      h2{font-size:1rem}
    }
  </style>
</head>
<body>

<!-- 🎭 HERO SECTION -->
<div class="hero">
  <div data-aos="zoom-in">
    <h1>REPLICA</h1>
    <h2>Act as the Video Plays 🎬</h2>

    <div class="meta">
      <div>📅 March 13</div>
      <div>📍 SNSCT, Coimbatore</div>
      <div>🎭 Department of IT Event</div>
    </div>

    <div class="countdown" id="countdown"></div>

    <button class="btn" onclick="window.open('https://forms.gle/sybt5ksuUCcnYJ93A','_blank')">
      🚀 Register Now
    </button>
  </div>
</div>

<!-- 🎬 EVENT DETAILS -->
<section>
  <div class="grid">
    <div class="card" data-aos="fade-up">
      <h3>How It Works</h3>
      <p>A video will play on screen. Participants must act it out in real-time!</p>
    </div>

    <div class="card" data-aos="fade-up">
      <h3>Show Your Talent</h3>
      <p>Bring out your acting skills, expressions, and creativity.</p>
    </div>

    <div class="card" data-aos="fade-up">
      <h3>Judging Criteria</h3>
      <p>Expression • Timing • Energy • Accuracy</p>
    </div>
  </div>
</section>

<!-- 👥 COORDINATORS -->
<footer>
  <h4>STUDENT COORDINATORS</h4>
  <p>SRIJITH | POOJA</p>
  <p>📞 9791471277</p>
</footer>

<!-- JS -->
<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script>
AOS.init();

// Countdown Timer
const eventDate = new Date('March 13, 2026 09:00:00').getTime();
setInterval(()=>{
  const now = new Date().getTime();
  const diff = eventDate - now;
  if(diff<0) return;
  const d=Math.floor(diff/(1000*60*60*24));
  const h=Math.floor((diff%(1000*60*60*24))/(1000*60*60));
  const m=Math.floor((diff%(1000*60*60))/(1000*60));
  document.getElementById('countdown').innerHTML = `
    <div class='time'><h3>${d}</h3><small>Days</small></div>
    <div class='time'><h3>${h}</h3><small>Hours</small></div>
    <div class='time'><h3>${m}</h3><small>Mins</small></div>`;
},1000);
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)