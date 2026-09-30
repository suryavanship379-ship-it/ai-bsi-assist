import Icon from './Icon.jsx'

const services = [
  { icon: 'book', title: 'Indian Standards', text: 'Documents that set out specifications and guidance for products, processes and services.' },
  { icon: 'certificate', title: 'Product Certification', text: 'Schemes that assess whether applicable products meet specified requirements.' },
  { icon: 'flask', title: 'Laboratory & Testing', text: 'Testing services that help check products against relevant requirements.' },
  { icon: 'hallmark', title: 'Hallmarking', text: 'A way to indicate the purity of precious metal articles under applicable schemes.' },
  { icon: 'users', title: 'Consumer Affairs', text: 'Information and channels that help consumers make informed choices.' },
  { icon: 'layers', title: 'Standards & BIS Services', text: 'Explore the wider set of standards-related resources and services.' },
]

export default function BISServices() {
  return <section className="services-section section-pad">
    <div className="container"><p className="section-kicker">EXPLORE THE ECOSYSTEM</p><div className="section-heading"><h2>What does BIS do?</h2><p>Different services, one shared purpose: helping people understand and work with standards.</p></div>
      <div className="service-grid">{services.map((service, index) => <article className="service-card" key={service.title}><div className="service-icon"><Icon name={service.icon} size={24} /></div><span className="service-number">0{index + 1}</span><h3>{service.title}</h3><p>{service.text}</p></article>)}</div>
    </div>
  </section>
}
