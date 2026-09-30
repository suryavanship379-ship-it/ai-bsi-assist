import { useRef, useState } from 'react'
import Icon from './Icon.jsx'

export default function ChatInput({ onSend, isLoading, draft, setDraft }) {
  const ref = useRef(null)
  const [focused, setFocused] = useState(false)
  function submit(e) {
    e.preventDefault()
    if (!draft.trim() || isLoading) return
    onSend(draft.trim())
    ref.current?.focus()
  }
  function onKeyDown(e) {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); submit(e) }
  }
  return <form className={`chat-composer ${focused ? 'composer-focused' : ''}`} onSubmit={submit}>
    <textarea ref={ref} rows="1" value={draft} onChange={e => setDraft(e.target.value)} onKeyDown={onKeyDown} onFocus={() => setFocused(true)} onBlur={() => setFocused(false)} placeholder="Describe a product or ask about BIS..." aria-label="Your message" />
    <button type="submit" disabled={!draft.trim() || isLoading} aria-label="Send message"><Icon name="send" size={19} /></button>
  </form>
}
