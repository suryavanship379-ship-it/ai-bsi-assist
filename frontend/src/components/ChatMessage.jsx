import Icon from './Icon.jsx'
import StandardCard from './StandardCard.jsx'
import ComplianceJourney from './ComplianceJourney.jsx'
import LabCard from './LabCard.jsx'
import AssistantMark from './AssistantMark.jsx'

export default function ChatMessage({ message }) {
  const assistant = message.role === 'assistant'
  return <div className={`message-row ${assistant ? 'assistant-row' : 'user-row'}`}>
    {assistant && <div className="message-avatar"><AssistantMark compact /></div>}
    <div className="message-content">
      {assistant && <div className="message-author">BIS Mitra <span>Assistant</span></div>}
      <div className={`message-bubble ${assistant ? 'assistant-bubble' : 'user-bubble'}`}>
        {message.text.split('\n').filter(Boolean).map((line, i) => <p key={i}>{line}</p>)}
      </div>
      {message.cards?.length > 0 && <div className="response-cards">{message.cards.map((card, i) => {
        if (card.type === 'standard') return <StandardCard key={i} data={card.data} />
        if (card.type === 'journey') return <ComplianceJourney key={i} data={card.data} />
        if (card.type === 'lab') return <LabCard key={i} data={card.data} />
        return null
      })}</div>}
      {message.suggestions?.length > 0 && <div className="followup-suggestions">{message.suggestions.map(s => <span key={s}>{s}</span>)}</div>}
    </div>
  </div>
}
