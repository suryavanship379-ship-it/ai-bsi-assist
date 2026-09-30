import { useState } from 'react'
import Brand from './Brand.jsx'
import Icon from './Icon.jsx'

export default function Navbar({ navigate }) {
  const [open, setOpen] = useState(false)
  function go(page) { setOpen(false); navigate(page) }
  function about() { setOpen(false); document.getElementById('about-bis')?.scrollIntoView({ behavior: 'smooth' }) }
  return <header className="site-header">
    <div className="container nav-inner">
      <Brand onClick={() => go('home')} />
      <button className="mobile-menu" aria-label="Toggle navigation" aria-expanded={open} onClick={() => setOpen(!open)}><Icon name="menu" /></button>
      <nav className={open ? 'nav-links open' : 'nav-links'} aria-label="Main navigation">
        <button className="nav-active" onClick={() => go('home')}>Home</button>
        <button onClick={about}>About BIS</button>
        <button onClick={() => go('chat')}>Chat</button>
        <button className="button button-dark nav-cta" onClick={() => go('chat')}>Open assistant <Icon name="arrow" size={16} /></button>
      </nav>
    </div>
  </header>
}
