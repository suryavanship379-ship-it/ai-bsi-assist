import { useEffect, useRef, useState } from 'react'
import Brand from '../components/Brand.jsx'
import Icon from '../components/Icon.jsx'
import ChatMessage from '../components/ChatMessage.jsx'
import ChatInput from '../components/ChatInput.jsx'
import AssistantMark from '../components/AssistantMark.jsx'
import { sendMessage } from '../services/api.js'

const welcome = {
  id: 'welcome', role: 'assistant', text: "Welcome to BIS Mitra. Ask me about Indian Standards, testing, certification, or a product you're planning to manufacture.",
}

const prompts = [
  { icon: 'search', label: 'Find a BIS Standard', query: 'Help me find a BIS Standard for my product.' },
  { icon: 'certificate', label: 'Certification Requirements', query: 'What are the BIS certification requirements for my product?' },
  { icon: 'flask', label: 'Testing Requirements', query: 'What testing requirements should I consider for my product?' },
  { icon: 'factory', label: 'Find a Laboratory', query: 'How can I find a relevant testing laboratory?' },
  { icon: 'question', label: 'Ask a Question', query: '' },
]

export default function Chat({ navigate }) {
  const [messages, setMessages] = useState([welcome])
  const [draft, setDraft] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const endRef = useRef(null)
  const inputWrapRef = useRef(null)

  useEffect(() => { endRef.current?.scrollIntoView({ behavior: 'smooth', block: 'end' }) }, [messages, isLoading])

  async function handleSend(text) {
    if (isLoading) return
    const userMessage = { id: crypto.randomUUID(), role: 'user', text }
    const history = [...messages, userMessage]
    setMessages(history)
    setDraft('')
    setIsLoading(true)
    try {
      const response = await sendMessage(text, history.map(({ role, text: content }) => ({ role, content })))
      setMessages(current => [...current, { id: crypto.randomUUID(), role: 'assistant', ...response }])
    } catch {
      setMessages(current => [...current, { id: crypto.randomUUID(), role: 'assistant', text: 'Something went wrong. Please try sending your question again.' }])
    } finally { setIsLoading(false) }
  }

  function choosePrompt(prompt) {
    setDraft(prompt.query)
    inputWrapRef.current?.querySelector('textarea')?.focus()
  }

  return <div className="chat-app">
    <header className="chat-header"><div className="chat-header-inner"><button className="back-button" onClick={() => navigate('home')} aria-label="Back to home"><Icon name="back" size={20} /></button><Brand onClick={() => navigate('home')} /><span className="chat-header-divider" /><div className="chat-header-title">AI Assistant for Indian Standards &amp; BIS Services</div><div className="chat-status"><span /> BIS Knowledge Assistant</div></div></header>
    <main className="chat-main"><div className="chat-intro"><div className="ai-presence"><AssistantMark active={isLoading} /><span className="ai-presence-label">BIS MITRA / AI ONLINE</span></div><p className="chat-intro-kicker">A SIMPLER STARTING POINT</p><h1>Ask about standards.<br /><span>Find your way forward.</span></h1><p>Explore Indian Standards and BIS services, one question at a time.</p></div>
      <div className="conversation" aria-live="polite">{messages.map(m => <ChatMessage key={m.id} message={m} />)}{isLoading && <div className="message-row assistant-row"><div className="message-avatar"><AssistantMark compact active /></div><div><div className="message-author">BIS Mitra <span>Assistant</span></div><div className="typing-indicator" aria-label="BIS Mitra is responding"><i /><i /><i /></div></div></div>}<div ref={endRef} /></div>
      {messages.length === 1 && <div className="starter-area"><div className="starter-label">TRY ASKING ABOUT</div><div className="starter-grid">{prompts.map(p => <button key={p.label} className="starter-chip" onClick={() => choosePrompt(p)}><Icon name={p.icon} size={18} /><span>{p.label}</span><Icon name="arrow" size={16} /></button>)}</div></div>}
    </main>
    <div className="composer-area"><div className="composer-inner" ref={inputWrapRef}><ChatInput draft={draft} setDraft={setDraft} isLoading={isLoading} onSend={handleSend} /><p className="composer-note">Demo responses only. Verify requirements and decisions with official BIS sources.</p></div></div>
  </div>
}
