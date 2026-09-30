/**
 * Frontend integration point for the future Flask API.
 * Contract: sendMessage(message, conversationHistory) =>
 * { text: string, cards?: Array<{ type: 'standard'|'journey'|'lab', data: object }> }
 * conversationHistory is an array of { role, content } objects.
 * Replace the mock implementation below with an HTTP request when the backend is ready.
 */
export async function sendMessage(message, conversationHistory = []) {
  await new Promise(resolve => setTimeout(resolve, 650))
  const q = message.toLowerCase()
  const previousUserText = conversationHistory.filter(item => item.role === 'user').map(item => item.content).join(' ').toLowerCase()
  const product = /stainless[- ]steel.*bottle/.test(previousUserText) ? 'stainless-steel water bottles' : 'your product'

  const journey = { type: 'journey', data: { steps: ['Product identified', 'Identify an applicable standard', 'Check scheme requirements', 'Arrange product testing', 'Prepare certification application', 'Confirm next steps with BIS'] } }
  const standard = { type: 'standard', data: { title: 'Standard to be identified', description: `The applicable Indian Standard for ${product} needs to be checked against official BIS information. No standard number is asserted in this demo.` } }
  const lab = { type: 'lab', data: { title: 'Find a suitable laboratory', location: 'Location to be confirmed', description: 'Check the official BIS laboratory directory or recognized laboratory listings for the relevant product and test scope.' } }

  if (/lab|where.*test/.test(q)) return { text: `For ${product}, the right laboratory depends on the applicable standard and the specific tests. You can check official BIS laboratory information and confirm the lab's scope before booking.`, cards: [lab] }
  if (/test|testing/.test(q)) return { text: `Testing requirements for ${product} depend on the applicable Indian Standard and scheme. First confirm the product category and standard, then review its specified tests and choose a laboratory with the right scope. This demo does not invent a test list.`, cards: [standard, lab] }
  if (/document|paperwork|application/.test(q)) return { text: `The documents needed for ${product} depend on the certification scheme. Usually the next step is to identify the correct scheme and read its current official application guidance, including any product and testing documents it asks for.`, cards: [journey] }
  if (/certif|license|licence|mandatory/.test(q)) return { text: `Whether certification is required for ${product} depends on its exact category and any applicable requirements. Identify the product and standard first, then confirm the current scheme and legal status with official BIS sources.`, cards: [standard, journey] }
  if (/standard|\bis\b|specification/.test(q)) return { text: `Let's find the Indian Standard relevant to ${product}. The exact product description, material and intended use matter. Once a BIS knowledge source is connected, this card can show a verified IS number, title and source.`, cards: [standard] }
  if (/hello|^hi\b|^hey\b/.test(q)) return { text: 'Hello! Tell me which product you are exploring, or ask about an Indian Standard, certification, testing or laboratories. I can walk through the process with you.' }
  return { text: `Sure! I can help you explore BIS information for ${product}. We can look at the applicable Indian Standard, testing needs, certification requirements, relevant laboratories and a possible compliance journey. This is an illustrative preview; verified details will appear once the BIS knowledge system is connected. What would you like to know first?`, cards: [standard, journey] }
}
