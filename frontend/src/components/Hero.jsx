import Icon from './Icon.jsx'

export default function Hero({ navigate }) {
  return <section className="hero">
    <div className="hero-grid container">
      <div className="hero-copy">
        <div className="eyebrow"><span className="eyebrow-mark" /> MAKING STANDARDS SIMPLE</div>
        <h1>Clarity on standards.<br /><em>Confidence in every step.</em></h1>
        <p className="hero-tagline">Your AI Guide to Indian Standards &amp; BIS Services</p>
        <p className="hero-description">Understand Indian Standards, certification, testing and BIS services through a simple conversational assistant.</p>
        <div className="hero-actions">
          <button className="button button-primary" onClick={() => navigate('chat')}>Chat with BIS Mitra <Icon name="arrow" size={18} /></button>
          <button className="button button-outline" onClick={() => document.getElementById('about-bis')?.scrollIntoView({ behavior: 'smooth' })}>Learn About BIS</button>
        </div>
        <p className="hero-note"><Icon name="shield" size={16} /> An independent informational guide to BIS services</p>
      </div>
      <div className="hero-visual" aria-label="Animated preview of a BIS Mitra conversation">
        <div className="visual-orbit orbit-one" /><div className="visual-orbit orbit-two" />
        <video className="hero-film" autoPlay muted loop playsInline preload="metadata" aria-hidden="true"><source src="/standards-loop.mp4" type="video/mp4" /></video>
        <div className="visual-card">
          <div className="visual-top"><span className="visual-avatar"><Icon name="spark" size={18} /></span><div><strong>BIS Mitra</strong><small>Here to help you find your way</small></div><span className="visual-online" /></div>
          <div className="preview-message preview-user">I want to manufacture a product. Where do I begin?</div>
          <div className="preview-message preview-bot"><span className="preview-mini-icon"><Icon name="spark" size={15} /></span><p>Let’s explore the relevant standards, testing needs and next steps together.</p></div>
          <div className="preview-tags"><span><Icon name="book" size={15} /> Standards</span><span><Icon name="flask" size={15} /> Testing</span><span><Icon name="certificate" size={15} /> Certification</span></div>
          <div className="preview-input">Ask your BIS question... <Icon name="arrow" size={17} /></div>
        </div>
        <div className="floating-label"><span><Icon name="check" size={15} /></span> A simpler way to get started</div>
      </div>
    </div>
  </section>
}
