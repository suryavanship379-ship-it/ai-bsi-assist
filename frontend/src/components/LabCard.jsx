import Icon from './Icon.jsx'

export default function LabCard({ data }) {
  return <article className="context-card"><div className="context-heading"><span className="context-icon"><Icon name="flask" size={18} /></span><span>LABORATORY SEARCH</span><span className="demo-pill">Demo preview</span></div><h3>{data.title}</h3><p>{data.description}</p><div className="card-foot"><span><Icon name="pin" size={14} /> {data.location}</span>{data.sourceUrl && <a href={data.sourceUrl} target="_blank" rel="noreferrer">View details <Icon name="external" size={14} /></a>}</div></article>
}
