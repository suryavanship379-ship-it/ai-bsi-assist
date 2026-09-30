import Icon from './Icon.jsx'

export default function BISInfo() {
  return <section className="intro-section section-pad" id="about-bis">
    <div className="container intro-grid">
      <div><p className="section-kicker">THE FOUNDATION</p><h2>What is <span>BIS?</span></h2></div>
      <div className="intro-text"><p>BIS stands for the <strong>Bureau of Indian Standards.</strong> It is India's National Standards Body and works on standardization, product certification, testing, hallmarking and consumer-related services.</p><div className="intro-caption"><Icon name="info" size={19} /><span>Think of BIS as a key part of how quality and safety are supported across products and services in India.</span></div></div>
    </div>
  </section>
}
