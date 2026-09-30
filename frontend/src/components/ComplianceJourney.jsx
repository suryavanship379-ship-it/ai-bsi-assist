import Icon from './Icon.jsx'

export default function ComplianceJourney({ data }) {
  return <article className="context-card journey-card"><div className="context-heading"><span className="context-icon"><Icon name="layers" size={18} /></span><span>ILLUSTRATIVE PROCESS</span><span className="demo-pill">Demo preview</span></div><h3>Your BIS journey</h3><ol>{data.steps.map((step, index) => <li key={step}><span className={index === 0 ? 'step-done' : 'step-number'}>{index === 0 ? <Icon name="check" size={14} /> : String(index + 1).padStart(2, '0')}</span><span>{step}</span></li>)}</ol><p className="card-muted">Actual steps depend on the product and applicable BIS scheme.</p></article>
}
