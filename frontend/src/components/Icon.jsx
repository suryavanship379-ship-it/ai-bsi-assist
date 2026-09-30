const paths = {
  arrow: <><path d="M5 12h14" /><path d="m13 6 6 6-6 6" /></>,
  back: <><path d="M19 12H5" /><path d="m11 18-6-6 6-6" /></>,
  spark: <><path d="m12 2 1.7 6.3L20 10l-6.3 1.7L12 18l-1.7-6.3L4 10l6.3-1.7L12 2Z" /><path d="m19 17 .6 2.4L22 20l-2.4.6L19 23l-.6-2.4L16 20l2.4-.6L19 17Z" /></>,
  book: <><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21V5.5Z" /><path d="M4 18.5A2.5 2.5 0 0 1 6.5 16H20" /><path d="M8 7h8M8 10h5" /></>,
  certificate: <><rect x="4" y="3" width="16" height="15" rx="2" /><path d="M8 8h8M8 12h5M9 18v4l3-2 3 2v-4" /></>,
  flask: <><path d="M9 3h6M10 3v7l-5.5 8.4A2 2 0 0 0 6.2 21h11.6a2 2 0 0 0 1.7-2.6L14 10V3" /><path d="M7 16h10" /></>,
  hallmark: <><path d="m12 2 8 4v6c0 5-3.4 8.2-8 10-4.6-1.8-8-5-8-10V6l8-4Z" /><path d="m8.5 12 2.3 2.3 4.7-4.7" /></>,
  users: <><circle cx="9" cy="8" r="3" /><path d="M3 20v-2a6 6 0 0 1 12 0v2H3ZM17 5a3 3 0 0 1 0 6M17 14a5 5 0 0 1 4 5v1h-3" /></>,
  layers: <><path d="m12 3 9 5-9 5-9-5 9-5ZM3 12l9 5 9-5M3 16l9 5 9-5" /></>,
  shield: <><path d="m12 2 8 4v6c0 5-3.4 8.2-8 10-4.6-1.8-8-5-8-10V6l8-4Z" /><path d="m9 12 2 2 4-4" /></>,
  check: <path d="m5 12 4 4L19 6" />,
  search: <><circle cx="10.5" cy="10.5" r="6.5" /><path d="m16 16 5 5" /></>,
  factory: <><path d="M3 21V10l6 3V9l6 4V5h6v16H3Z" /><path d="M7 17h1M12 17h1M17 17h1" /></>,
  question: <><circle cx="12" cy="12" r="9" /><path d="M9.5 9a2.5 2.5 0 0 1 5 0c0 2-2.5 2-2.5 4M12 17h.01" /></>,
  send: <><path d="m21 3-8.5 18-2.3-7.2L3 11.5 21 3ZM10.2 13.8 21 3" /></>,
  external: <><path d="M13 4h7v7M20 4l-9 9" /><path d="M20 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h5" /></>,
  pin: <><path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 0 1 16 0Z" /><circle cx="12" cy="10" r="2.5" /></>,
  info: <><circle cx="12" cy="12" r="9" /><path d="M12 11v5M12 8h.01" /></>,
  menu: <><path d="M4 7h16M4 12h16M4 17h16" /></>,
}

export default function Icon({ name, size = 20, strokeWidth = 1.8, ...props }) {
  return <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={strokeWidth} strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" {...props}>{paths[name]}</svg>
}
