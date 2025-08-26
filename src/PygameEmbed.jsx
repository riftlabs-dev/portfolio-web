// src/PygameEmbed.jsx
import React from 'react';

function PygameEmbed() {
  return (
    <iframe
      src="/pygbag/index.html"
      title="Space Shooter"
      width="800"
      height="600"
      style={{ border: 'none', borderRadius: '8px', width: '100%', maxWidth: '800px' }}
    />
  );
}

export default PygameEmbed;