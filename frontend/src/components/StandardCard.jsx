import Icon from './Icon.jsx'

export default function StandardCard({ data }) {
  return <article className="context-card"><div className="context-heading"><span className="context-icon"><Icon name="book" size={18} /></span><span>APPLICABLE STANDARD</span><span className="demo-pill">Demo preview</span></div><h3>{data.title}</h3><p>{data.description}</p><div className="card-foot"><span>IS number and source pending verification</span>{data.sourceUrl && <a href={data.sourceUrl} target="_blank" rel="noreferrer">View official source <Icon name="external" size={14} /></a>}</div></article>
}
