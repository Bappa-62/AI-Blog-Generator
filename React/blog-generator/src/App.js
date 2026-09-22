import React, { useState } from "react";
import api from "./Api"; /*  Axios Object -> which is a JavaScript library used to make HTTP requests. */
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [language, setLanguage] = useState("English");
  const [tone, setTone] = useState("Technical");
  const [wordCount, setWordCount] = useState(500);

  const [generateX, setGenerateX] = useState(false);
  const [generateLinkedIn, setGenerateLinkedIn] = useState(false);
  const [generateInstagram, setGenerateInstagram] = useState(false);

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const generateBlog = async () => {
    if (!topic.trim()) {
      setError("Please enter a topic.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await api.post("/generate-blogs", {  /* This is where http://localhost:8000/generate-blogs (Fast API) is getting called */
        topic: topic,
        language: language,
        tone: tone,
        word_count: Number(wordCount),
        generate_x: generateX,
        generate_linkedin: generateLinkedIn,
        generate_instagram: generateInstagram,
      });

      console.log("API Response:", response.data);

      setResult(response.data.data);

    } catch (error) {
      console.error("API Error:", error);

      if (error.response) {
        setError(
          error.response.data?.detail ||
          `Server error: ${error.response.status}`
        );
      } else if (error.request) {
        setError(
          "Unable to connect to the FastAPI server. Make sure it is running on port 8000."
        );
      } else {
        setError("Something went wrong.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      <div className="container">

        {/* Header */}
        <div className="header">
          <h1>AI Blog Generator</h1>

          <p>
            Generate AI-powered blogs and social media content
            using intelligent workflows.
          </p>
        </div>

        {/* Input Section */}
        <div className="input-section">

          {/* Topic */}
          <div className="form-group">
            <label>Blog Topic</label>

            <input
              type="text"
              placeholder="Enter your blog topic..."
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
            />
          </div>

          {/* Language */}
          <div className="form-group">
            <label>Language</label>

            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
            >
              <option value="English">English</option>
              <option value="Hindi">Hindi</option>
              <option value="Bengali">Bengali</option>
              <option value="Spanish">Spanish</option>
              <option value="French">French</option>
              <option value="German">German</option>
              <option value="Chinese">Chinese</option>
              <option value="Russian">Russian</option>
              <option value="Korean">Korean</option>
              <option value="Japanese">Japanese</option>
              <option value="Arabic">Arabic</option>
              <option value="Portuguese">Portuguese</option>
              <option value="Italian">Italian</option>
            </select>
          </div>

          {/* Tone */}
          <div className="form-group">
            <label>Tone</label>

            <select
              value={tone}
              onChange={(e) => setTone(e.target.value)}
            >
              <option value="Technical">Technical</option>
              <option value="Professional">Professional</option>
              <option value="Educational">Educational</option>
              <option value="Friendly">Friendly</option>
              <option value="Casual">Casual</option>
              <option value="Creative">Creative</option>
            </select>
          </div>

          {/* Word Count */}
          <div className="form-group">
            <label>Word Count</label>

            <input
              type="number"
              min="50"
              max="5000"
              value={wordCount}
              onChange={(e) => setWordCount(e.target.value)}
            />
          </div>

          {/* Social Media */}
          <div className="form-group">

            <label>Generate Social Media Content</label>

            <div className="checkbox-group">

              <label className="checkbox-label">
                <input
                  type="checkbox"
                  checked={generateX}
                  onChange={(e) =>
                    setGenerateX(e.target.checked)
                  }
                />
                X / Twitter
              </label>

              <label className="checkbox-label">
                <input
                  type="checkbox"
                  checked={generateLinkedIn}
                  onChange={(e) =>
                    setGenerateLinkedIn(e.target.checked)
                  }
                />
                LinkedIn
              </label>

              <label className="checkbox-label">
                <input
                  type="checkbox"
                  checked={generateInstagram}
                  onChange={(e) =>
                    setGenerateInstagram(e.target.checked)
                  }
                />
                Instagram
              </label>

            </div>
          </div>

          {/* Generate Button */}
          <button
            className="generate-button"
            onClick={generateBlog}
            disabled={loading}
          >
            {loading ? "Generating..." : "Generate Blog"}
          </button>

        </div>

        {/* Error */}
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {/* Results */}
        {result && (
          <div className="results">

            {/* Blog */}
            {result.blog && (
              <div className="result-card">

                <div className="card-header">
                  <h2>{result.blog.title}</h2>

                  <div className="metadata">
                    <span>{result.language}</span>
                    <span>{result.tone}</span>
                    <span>{result.word_count} words</span>
                  </div>
                </div>

                <div className="blog-content">
                  <p>{result.blog.content}</p>
                </div>

              </div>
            )}

            {/* Social Media */}
            {result.social_media && (
              <div className="social-section">

                <h2>Social Media Content</h2>

                {/* LinkedIn */}
                {result.generate_linkedin &&
                  result.social_media.linkedin && (
                    <div className="social-card">

                      <h3>LinkedIn</h3>

                      <p>
                        {result.social_media.linkedin}
                      </p>

                    </div>
                  )}

                {/* X */}
                {result.generate_x &&
                  result.social_media.twitter && (
                    <div className="social-card">

                      <h3>X / Twitter</h3>

                      <p>
                        {result.social_media.twitter}
                      </p>

                    </div>
                  )}

                {/* Instagram */}
                {result.generate_instagram &&
                  result.social_media.instagram && (
                    <div className="social-card">

                      <h3>Instagram</h3>

                      <p>
                        {result.social_media.instagram}
                      </p>

                    </div>
                  )}

              </div>
            )}

          </div>
        )}

      </div>

    </div>
  );
}

export default App;