import { useEffect } from 'react'
import Navbar from '../components/Navbar.jsx'
import Hero from '../components/Hero.jsx'
import BISInfo from '../components/BISInfo.jsx'
import BISServices from '../components/BISServices.jsx'
import Brand from '../components/Brand.jsx'
import Icon from '../components/Icon.jsx'

const benefits = [
  { number: '01', title: 'Quality', text: 'Clear expectations can help products meet consistent specifications.' },
  { number: '02', title: 'Safety', text: 'Relevant requirements can help address risks in everyday use.' },
  { number: '03', title: 'Reliability', text: 'Common benchmarks help build confidence in product performance.' },
  { number: '04', title: 'Consumer protection', text: 'Standards support more informed choices and greater trust.' },
]

export default function Home({ navigate }) {
  useEffect(() => {
    const elements = document.querySelectorAll('.intro-grid > *, .section-heading > *, .service-card, .benefits-intro, .benefits-list article, .mitra-art, .mitra-copy, .cta-layout > *')
    if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    elements.forEach((element, index) => {
      element.classList.add('scroll-reveal')
      element.style.setProperty('--reveal-x', index % 2 ? '46px' : '-46px')
    })
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
          observer.unobserve(entry.target)
        }
      })
    }, { threshold: .12, rootMargin: '0px 0px -35px 0px' })
    elements.forEach(element => observer.observe(element))
    return () => observer.disconnect()
  }, [])
  return <>
    <Navbar navigate={navigate} />
    <main>
      <Hero navigate={navigate} />
      <section className="motion-showcase" aria-label="Standards and certification visual"><video autoPlay muted loop playsInline preload="metadata" aria-hidden="true"><source src="/standards-loop.mp4" type="video/mp4" /></video><div className="motion-showcase-shade" /><div className="container motion-showcase-content"><span className="film-index">01 / SYSTEM VISUAL</span><div><p className="section-kicker">EXPLORE THE PROCESS</p><h2>From a question<br />to a clearer path.</h2><p>Standards · Testing · Certification · Next steps</p></div><span className="film-status"><i /> LIVE VISUAL</span></div></section>
      <BISInfo />
      <BISServices />
      <section className="benefits-section section-pad"><div className="container benefits-layout"><div className="benefits-intro"><p className="section-kicker">WHY IT MATTERS</p><h2>Built on trust.<br /><span>Made for everyone.</span></h2><p>Standards help set shared expectations that matter to businesses, consumers and communities.</p><div className="benefits-deco"><Icon name="shield" size={48} strokeWidth={1.2} /></div></div><div className="benefits-list">{benefits.map(b => <article key={b.number}><span>{b.number}</span><div><h3>{b.title}</h3><p>{b.text}</p></div><Icon name="arrow" size={19} /></article>)}</div></div></section>
      <section className="mitra-section section-pad"><div className="container mitra-layout"><div className="mitra-art" aria-hidden="true"><div className="art-ring ring-a" /><div className="art-ring ring-b" /><div className="art-center"><Icon name="spark" size={46} /></div><div className="art-label art-label-a"><Icon name="search" size={17} /> Explore</div><div className="art-label art-label-b"><Icon name="book" size={17} /> Understand</div><div className="art-label art-label-c"><Icon name="check" size={17} /> Take the next step</div></div><div className="mitra-copy"><p className="section-kicker">MEET YOUR GUIDE</p><h2>What is <span>BIS Mitra?</span></h2><p>BIS Mitra makes BIS information easier to understand. Describe a product or ask a question, and it can guide you toward relevant standards, requirements, testing, certification and next steps.</p><div className="disclaimer"><Icon name="info" size={20} /><span>BIS Mitra provides information based on available BIS sources and does not replace official BIS decisions or approvals.</span></div></div></div></section>
      <section className="cta-section"><div className="container cta-layout"><div><p className="section-kicker">YOUR NEXT STEP</p><h2>Have a BIS-related<br />question?</h2><p>Tell BIS Mitra what product you're working with or ask your question directly.</p></div><button className="button button-light" onClick={() => navigate('chat')}>Start chatting <Icon name="arrow" size={19} /></button></div></section>
    </main>
    <footer className="site-footer"><div className="container footer-main"><div><Brand onClick={() => navigate('home')} /><p>A simpler starting point for Indian Standards and BIS services.</p></div><div className="footer-links"><button onClick={() => navigate('home')}>Home</button><button onClick={() => navigate('chat')}>Chat with BIS Mitra</button><a href="https://www.bis.gov.in/" target="_blank" rel="noreferrer">Official BIS website <Icon name="external" size={14} /></a></div></div><div className="container footer-bottom"><span>© {new Date().getFullYear()} BIS Mitra · Student project prototype</span><span>Independent informational tool · Not an official BIS service</span></div></footer>
  </>
}
