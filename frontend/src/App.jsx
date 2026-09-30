import { useEffect, useState } from 'react'
import Home from './pages/Home.jsx'
import Chat from './pages/Chat.jsx'

function pageFromPath() {
  return window.location.pathname === '/chat' ? 'chat' : 'home'
}

export default function App() {
  const [page, setPage] = useState(pageFromPath)

  useEffect(() => {
    const onPopState = () => setPage(pageFromPath())
    window.addEventListener('popstate', onPopState)
    return () => window.removeEventListener('popstate', onPopState)
  }, [])

  function navigate(nextPage) {
    const path = nextPage === 'chat' ? '/chat' : '/'
    if (window.location.pathname !== path) window.history.pushState({}, '', path)
    setPage(nextPage)
    window.scrollTo({ top: 0, behavior: 'instant' })
  }

  return page === 'chat' ? <Chat navigate={navigate} /> : <Home navigate={navigate} />
}
