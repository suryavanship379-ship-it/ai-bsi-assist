export default function AssistantMark({ compact = false, active = false }) {
  return <span className={`assistant-mark ${compact ? 'assistant-mark-compact' : ''} ${active ? 'assistant-mark-active' : ''}`} aria-hidden="true">
    <span className="assistant-mark-ring ring-outer" />
    <span className="assistant-mark-ring ring-inner" />
    <span className="assistant-mark-core" />
    <span className="assistant-mark-scan" />
  </span>
}
