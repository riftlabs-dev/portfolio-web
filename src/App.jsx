import './App.css'
import PygameEmbed from './PygameEmbed';

function App() {
  return (
    <>
      <div class='container'>
        <div>
          {/* <h2>Software and Data Projects</h2> */}
          <img src="/gif-1.gif" alt="Portfolio" class="fade-in"style={{ borderRadius: '8px', width: '100%', maxWidth: '320px' }} />
          
        </div>
        <div class="dropdown fade-in">
          <button class="dropbtn">Software & Data Analysis</button>
          <div class="dropdown-content">
            <a href="/gll.html" target="_blank">1 - Geospatial Landslide Locator</a>
            <a href="https://philosopher-bot-frontend.vercel.app/" target="_blank">2 - Philosophy Chatbot</a>
            <a href="/gll.html" target="_blank">3 - River Toxicity Analysis</a>
            <a href="/pygbag/index.html" target="_blank">4 - Space Shooter</a>
          </div>
        </div>
      </div>
    </>  
  )
}

export default App

