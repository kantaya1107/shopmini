<template>
  <main class="home-page">
    <div class="background-glow background-glow--top" aria-hidden="true"></div>
    <div class="background-glow background-glow--bottom" aria-hidden="true"></div>

    <header class="site-header">
      <RouterLink class="brand" to="/" aria-label="ShopMini หน้าหลัก">
        <span class="brand-mark">s</span>
        <span>shop<span class="brand-accent">mini</span></span>
      </RouterLink>

      <nav class="header-nav" aria-label="เมนูหลัก">
        <RouterLink class="nav-link nav-link--active" to="/">หน้าหลัก</RouterLink>
        <RouterLink class="nav-link" to="/products">สินค้าทั้งหมด</RouterLink>
      </nav>

      <RouterLink class="header-button" to="/products">
        เลือกซื้อสินค้า <span aria-hidden="true">↗</span>
      </RouterLink>
    </header>

    <section class="hero">
      <div class="hero-copy">
        <div class="eyebrow"><span class="eyebrow-dot"></span> ของดีใกล้ตัว ในราคาที่ใช่</div>
        <h1>เติมความสุข<br />ให้ทุกวัน<span class="title-accent">ง่ายขึ้น</span></h1>
        <p class="hero-description">
          เลือกช้อปสินค้าชิ้นโปรดได้ง่าย ๆ ในที่เดียว<br class="desktop-break" />
          คัดสรรมาแล้วเพื่อวันที่ดีของคุณ
        </p>
        <div class="hero-actions">
          <RouterLink class="primary-button" to="/products">
            เริ่มเลือกซื้อ <span aria-hidden="true">→</span>
          </RouterLink>
          <span class="shipping-note"><span aria-hidden="true">✦</span> ช้อปเพลิน ส่งตรงถึงบ้าน</span>
        </div>
        <div class="social-proof">
          <div class="avatar-stack" aria-hidden="true">
            <span>😊</span><span>🙂</span><span>😎</span>
          </div>
          <p><strong>ช้อปง่าย สบายใจ</strong><br />สินค้าคุณภาพที่คัดมาเพื่อคุณ</p>
        </div>
      </div>

      <div class="hero-art" aria-label="ภาพประกอบสินค้าช้อปปิ้ง">
        <div class="art-sun"></div>
        <span class="sparkle sparkle--one" aria-hidden="true">✦</span>
        <span class="sparkle sparkle--two" aria-hidden="true">✧</span>
        <span class="art-tag">GOOD<br />FINDS</span>
        <div class="shopping-bag">
          <div class="bag-handle"></div>
          <div class="bag-face">
            <span class="bag-logo">s</span>
            <span class="bag-smile">⌣</span>
          </div>
        </div>
        <div class="floating-card floating-card--plant" aria-hidden="true">🌿</div>
        <div class="floating-card floating-card--heart" aria-hidden="true">♥</div>
        <div class="art-caption"><span class="caption-dot"></span> คัดสรรด้วยใจ</div>
      </div>
    </section>

    <section class="highlights" aria-label="จุดเด่นของ ShopMini">
      <article class="highlight-card">
        <span class="highlight-icon highlight-icon--mint" aria-hidden="true">✿</span>
        <div>
          <h2>เลือกมาเพื่อคุณ</h2>
          <p>สินค้าน่าใช้ คัดสรรอย่างตั้งใจ</p>
        </div>
      </article>
      <article class="highlight-card">
        <span class="highlight-icon highlight-icon--peach" aria-hidden="true">♡</span>
        <div>
          <h2>ช้อปง่ายทุกวัน</h2>
          <p>ค้นหาสิ่งที่ชอบได้ในไม่กี่คลิก</p>
        </div>
      </article>
      <article class="highlight-card">
        <span class="highlight-icon highlight-icon--lavender" aria-hidden="true">✦</span>
        <div>
          <h2>คุ้มค่า น่าประทับใจ</h2>
          <p>เติมรอยยิ้มให้ทุกการเลือกซื้อ</p>
        </div>
      </article>
    </section>

    <footer class="home-footer">
      <span>ShopMini — small finds, happy days</span>
      <RouterLink to="/products">ค้นพบสินค้าของเรา <span aria-hidden="true">→</span></RouterLink>
    </footer>
  </main>
</template>

<style scoped>
.home-page {
  --ink: #203b35;
  --muted: #74837b;
  --green: #347b62;
  --green-dark: #28634e;
  position: relative;
  isolation: isolate;
  min-height: 100vh;
  overflow: hidden;
  padding: 0 clamp(1.25rem, 7.5vw, 7.5rem);
  color: var(--ink);
  background:
    radial-gradient(ellipse at 50% 100%, rgba(244, 225, 198, 0.38), transparent 40%),
    #f8f7f1;
  font-family: "MMM", "Google_san", sans-serif;
}

.background-glow {
  position: absolute;
  z-index: -1;
  width: 24rem;
  aspect-ratio: 1;
  border-radius: 50%;
  filter: blur(1px);
  pointer-events: none;
}

.background-glow--top {
  top: -16rem;
  right: -4rem;
  background: rgba(205, 231, 212, 0.38);
}

.background-glow--bottom {
  bottom: 4rem;
  left: -18rem;
  background: rgba(252, 222, 202, 0.34);
}

.site-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 5.75rem;
  border-bottom: 1px solid rgba(43, 72, 60, 0.09);
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  color: var(--ink);
  font-family: "Google_san", "MMM", sans-serif;
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.06em;
  text-decoration: none;
}

.brand-mark {
  display: grid;
  width: 2rem;
  aspect-ratio: 1;
  place-items: center;
  border-radius: 0.7rem;
  color: #fffdf8;
  background: var(--green);
  font-family: "MMM", sans-serif;
  font-size: 1.35rem;
}

.brand-accent {
  color: var(--green);
}

.header-nav {
  display: flex;
  gap: clamp(1.25rem, 3vw, 2.8rem);
}

.nav-link {
  color: #758078;
  font-size: 0.88rem;
  text-decoration: none;
  transition: color 160ms ease;
}

.nav-link:hover,
.nav-link--active {
  color: var(--green-dark);
}

.header-button,
.primary-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  border-radius: 999px;
  color: white;
  background: var(--green);
  font-size: 0.85rem;
  text-decoration: none;
  transition: background 160ms ease, transform 160ms ease, box-shadow 160ms ease;
}

.header-button {
  padding: 0.75rem 1.15rem;
}

.header-button:hover,
.primary-button:hover {
  transform: translateY(-2px);
  background: var(--green-dark);
  box-shadow: 0 0.6rem 1.3rem rgba(40, 99, 78, 0.18);
}

.hero {
  display: grid;
  grid-template-columns: 1fr 0.9fr;
  align-items: center;
  gap: 3rem;
  max-width: 68rem;
  min-height: 33.5rem;
  margin: 0 auto;
  padding: 2rem 0 1.5rem;
}

.hero-copy {
  padding: 1rem 0 0 0.5rem;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  margin-bottom: 1.25rem;
  color: var(--green);
  font-size: 0.78rem;
}

.eyebrow-dot,
.caption-dot {
  width: 0.45rem;
  aspect-ratio: 1;
  border-radius: 50%;
  background: #8db89b;
  box-shadow: 0 0 0 0.25rem rgba(141, 184, 155, 0.17);
}

h1 {
  margin: 0;
  color: var(--ink);
  font-size: clamp(3rem, 6.1vw, 5.25rem);
  font-weight: 600;
  letter-spacing: -0.055em;
  line-height: 1.15;
}

.title-accent {
  display: inline-block;
  margin-left: 0.18em;
  color: var(--green);
}

.hero-description {
  margin: 1.25rem 0 1.8rem;
  color: var(--muted);
  font-size: 0.98rem;
  line-height: 1.9;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1.3rem;
}

.primary-button {
  min-height: 3.15rem;
  padding: 0 1.5rem;
  box-shadow: 0 0.5rem 1.2rem rgba(40, 99, 78, 0.16);
}

.shipping-note {
  color: #78847b;
  font-size: 0.75rem;
}

.shipping-note span {
  margin-right: 0.25rem;
  color: #d5a461;
}

.social-proof {
  display: flex;
  align-items: center;
  gap: 0.9rem;
  margin-top: 2.7rem;
}

.avatar-stack {
  display: flex;
  padding-left: 0.25rem;
}

.avatar-stack span {
  display: grid;
  width: 2rem;
  aspect-ratio: 1;
  place-items: center;
  margin-left: -0.25rem;
  border: 2px solid #f8f7f1;
  border-radius: 50%;
  background: #e5eee1;
  font-size: 0.88rem;
}

.avatar-stack span:nth-child(2) {
  background: #f4dfcf;
}

.avatar-stack span:nth-child(3) {
  background: #e5e3f1;
}

.social-proof p {
  margin: 0;
  color: #879087;
  font-size: 0.68rem;
  line-height: 1.7;
}

.social-proof strong {
  color: #4d6257;
  font-size: 0.75rem;
  font-weight: 500;
}

.hero-art {
  position: relative;
  display: grid;
  min-height: 27rem;
  place-items: center;
}

.art-sun {
  position: absolute;
  width: min(25rem, 92%);
  aspect-ratio: 1;
  border-radius: 48% 52% 51% 49% / 46% 44% 56% 54%;
  background: #e3eee1;
  transform: rotate(-8deg);
}

.art-sun::after {
  position: absolute;
  inset: 1rem -0.7rem -0.55rem 0.7rem;
  border: 1px solid rgba(78, 130, 99, 0.24);
  border-radius: inherit;
  content: "";
  transform: rotate(13deg);
}

.shopping-bag {
  position: relative;
  z-index: 1;
  width: 12.8rem;
  transform: rotate(-7deg);
  filter: drop-shadow(0 1.3rem 1.2rem rgba(46, 88, 67, 0.15));
}

.bag-handle {
  width: 4.5rem;
  height: 3.1rem;
  margin: 0 auto -0.6rem;
  border: 0.55rem solid #b66e48;
  border-bottom: 0;
  border-radius: 2.8rem 2.8rem 0 0;
}

.bag-face {
  display: flex;
  height: 13.2rem;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 0.75rem 0.75rem 1.4rem 1.4rem;
  color: #fff9eb;
  background: linear-gradient(145deg, #e69b6e, #cf8058);
  clip-path: polygon(5% 0, 95% 0, 100% 100%, 0 100%);
}

.bag-logo {
  display: grid;
  width: 3.2rem;
  aspect-ratio: 1;
  place-items: center;
  border: 1px solid rgba(255, 249, 235, 0.67);
  border-radius: 1rem;
  font-size: 2.1rem;
}

.bag-smile {
  margin-top: -0.25rem;
  font-family: sans-serif;
  font-size: 2.6rem;
  line-height: 1;
}

.art-tag {
  position: absolute;
  z-index: 2;
  top: 18%;
  right: 2%;
  display: grid;
  width: 4.3rem;
  aspect-ratio: 1;
  place-items: center;
  border: 1px solid rgba(196, 151, 87, 0.4);
  border-radius: 50%;
  color: #aa7941;
  background: #f8efd9;
  font-family: "Google_san", sans-serif;
  font-size: 0.6rem;
  font-weight: 700;
  line-height: 1.3;
  text-align: center;
  transform: rotate(12deg);
}

.sparkle {
  position: absolute;
  z-index: 2;
  color: #c4985d;
}

.sparkle--one {
  top: 23%;
  left: 13%;
  font-size: 1.7rem;
}

.sparkle--two {
  right: 10%;
  bottom: 23%;
  color: #72977a;
  font-size: 2.1rem;
}

.floating-card {
  position: absolute;
  z-index: 2;
  display: grid;
  width: 3.5rem;
  aspect-ratio: 1;
  place-items: center;
  border: 1px solid rgba(68, 91, 72, 0.08);
  border-radius: 1.1rem;
  background: rgba(255, 253, 247, 0.92);
  box-shadow: 0 0.7rem 1.8rem rgba(62, 84, 63, 0.1);
  font-size: 1.35rem;
}

.floating-card--plant {
  top: 34%;
  left: 8%;
  transform: rotate(-12deg);
}

.floating-card--heart {
  right: 7%;
  bottom: 31%;
  color: #d98973;
  transform: rotate(10deg);
}

.art-caption {
  position: absolute;
  right: 15%;
  bottom: 5%;
  display: flex;
  align-items: center;
  gap: 0.55rem;
  color: #718078;
  font-size: 0.74rem;
}

.caption-dot {
  width: 0.35rem;
  background: #d18a67;
  box-shadow: none;
}

.highlights {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  max-width: 68rem;
  margin: 0 auto;
  border: 1px solid rgba(49, 77, 62, 0.08);
  border-radius: 1.3rem;
  background: rgba(255, 255, 251, 0.7);
  box-shadow: 0 1rem 3rem rgba(54, 77, 59, 0.035);
}

.highlight-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  min-height: 6.2rem;
  padding: 1rem 1.5rem;
}

.highlight-card + .highlight-card {
  border-left: 1px solid rgba(49, 77, 62, 0.08);
}

.highlight-icon {
  display: grid;
  width: 2.7rem;
  flex: 0 0 2.7rem;
  aspect-ratio: 1;
  place-items: center;
  border-radius: 0.9rem;
  font-size: 1.25rem;
}

.highlight-icon--mint {
  color: #46816a;
  background: #e4f0e5;
}

.highlight-icon--peach {
  color: #c97d62;
  background: #f8e8de;
}

.highlight-icon--lavender {
  color: #8471a3;
  background: #eee9f5;
}

.highlight-card h2 {
  margin: 0 0 0.2rem;
  color: #33483d;
  font-size: 0.85rem;
  font-weight: 500;
}

.highlight-card p {
  margin: 0;
  color: #899188;
  font-size: 0.69rem;
}

.home-footer {
  display: flex;
  justify-content: space-between;
  max-width: 68rem;
  margin: 1.7rem auto 0;
  padding-bottom: 1.5rem;
  color: #9aa198;
  font-family: "Google_san", sans-serif;
  font-size: 0.67rem;
}

.home-footer a {
  color: var(--green);
  text-decoration: none;
}

.home-footer a:hover {
  color: var(--green-dark);
}

@media (max-width: 760px) {
  .home-page {
    padding: 0 1.25rem;
  }

  .site-header {
    min-height: 4.6rem;
  }

  .header-nav {
    gap: 1rem;
  }

  .nav-link {
    font-size: 0.76rem;
  }

  .header-button {
    display: none;
  }

  .hero {
    grid-template-columns: 1fr 0.85fr;
    min-height: auto;
    gap: 0.5rem;
    padding: 3.5rem 0 2rem;
  }

  .hero-copy {
    position: relative;
    z-index: 3;
    padding-left: 0;
  }

  h1 {
    font-size: clamp(2.6rem, 8vw, 4rem);
  }

  .hero-description {
    font-size: 0.86rem;
  }

  .hero-art {
    min-height: 22rem;
  }

  .shopping-bag {
    width: 9rem;
  }

  .bag-face {
    height: 10rem;
  }

  .art-tag {
    right: 0;
  }

  .floating-card--plant {
    left: 0;
  }

  .highlights {
    grid-template-columns: 1fr;
  }

  .highlight-card {
    min-height: 5.1rem;
  }

  .highlight-card + .highlight-card {
    border-top: 1px solid rgba(49, 77, 62, 0.08);
    border-left: 0;
  }
}

@media (max-width: 520px) {
  .brand {
    font-size: 1.15rem;
  }

  .header-nav {
    gap: 0.75rem;
  }

  .nav-link {
    font-size: 0.68rem;
  }

  .hero {
    grid-template-columns: 1fr;
    padding-top: 3rem;
  }

  .hero-copy {
    text-align: center;
  }

  .eyebrow,
  .hero-actions,
  .social-proof {
    justify-content: center;
  }

  .hero-description {
    margin-top: 1rem;
  }

  .desktop-break {
    display: none;
  }

  .social-proof {
    margin-top: 1.7rem;
  }

  .hero-art {
    min-height: 21rem;
    margin-top: -0.5rem;
  }

  .art-caption {
    right: 18%;
    bottom: 3%;
  }

  .home-footer {
    gap: 1rem;
    font-size: 0.62rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
</style>
