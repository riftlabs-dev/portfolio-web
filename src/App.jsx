import './App.css'

function App() {
  return (
    <>
      <div class='container'>
        <div>
          {/* <h2>Software and Data Projects</h2> */}
          <img src="/gif-1.gif" alt="Portfolio" style={{ borderRadius: '8px', width: '100%', maxWidth: '320px' }} />
          
        </div>
        <div class="dropdown">
          <button class="dropbtn">Software & Data Analysis</button>
          <div class="dropdown-content">
            <a href="/gll.html" target="_blank">1 - Geospatial Landslide Locator</a>
            <a href="https://philosopher-bot-frontend.vercel.app/" target="_blank">2 - Philosophy Chatbot</a>
          </div>
        </div>
      </div>
    </>
  )
}

export default App

