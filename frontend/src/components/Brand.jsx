import Icon from './Icon.jsx'

export default function Brand({ light = false, onClick }) {
  return <button className={`brand ${light ? 'brand-light' : ''}`} onClick={onClick} aria-label="BIS Mitra home">
    <span className="brand-symbol"><Icon name="spark" size={24} strokeWidth={2} /></span>
    <span>BIS <strong>Mitra</strong></span>
  </button>
}
