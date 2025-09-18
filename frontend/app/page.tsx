"use client"

import { useState } from "react"

export default function Home() {
  const [userPrompt, setUserPrompt] = useState("")
  const [sqlQuery, setSqlQuery] = useState("")
  const [llmResponse, setLlmResponse] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  const handlePromptSubmit = async () => {
    if (!userPrompt.trim()) return

    setIsLoading(true)
    setSqlQuery("SELECT * FROM dataset.table WHERE condition = 'example'")
    setIsLoading(false)
  }

  const handleExecuteQuery = async () => {
    if (!sqlQuery.trim()) return

    setIsLoading(true)
    setLlmResponse("Based on the query results, here is the analysis of your data...")
    setIsLoading(false)
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 p-8">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold text-center mb-12 text-gray-800 dark:text-gray-100">
          BigQuery LLM Pipeline
        </h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 flex flex-col">
            <h2 className="text-lg font-semibold mb-4 text-gray-700 dark:text-gray-200">
              User Prompt
            </h2>
            <textarea
              value={userPrompt}
              onChange={(e) => setUserPrompt(e.target.value)}
              placeholder="Enter your question about the data..."
              className="flex-1 w-full p-4 border border-gray-300 dark:border-gray-600 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-50 dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              rows={10}
            />
            <button
              onClick={handlePromptSubmit}
              disabled={isLoading || !userPrompt.trim()}
              className="mt-4 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors font-medium"
            >
              Enter Prompt
            </button>
          </div>

          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 flex flex-col">
            <h2 className="text-lg font-semibold mb-4 text-gray-700 dark:text-gray-200">
              SQL Query
            </h2>
            <textarea
              value={sqlQuery}
              onChange={(e) => setSqlQuery(e.target.value)}
              placeholder="Generated SQL query will appear here..."
              className="flex-1 w-full p-4 border border-gray-300 dark:border-gray-600 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-green-500 bg-gray-50 dark:bg-gray-700 text-gray-800 dark:text-gray-200 font-mono text-sm"
              rows={10}
            />
            <button
              onClick={handleExecuteQuery}
              disabled={isLoading || !sqlQuery.trim()}
              className="mt-4 px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors font-medium"
            >
              Execute Query
            </button>
          </div>

          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 flex flex-col">
            <h2 className="text-lg font-semibold mb-4 text-gray-700 dark:text-gray-200">
              Response
            </h2>
            <div className="flex-1 w-full p-4 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 overflow-auto">
              {llmResponse ? (
                <p className="text-gray-800 dark:text-gray-200 whitespace-pre-wrap">
                  {llmResponse}
                </p>
              ) : (
                <p className="text-gray-500 dark:text-gray-400 italic">
                  Natural language response will appear here...
                </p>
              )}
            </div>
          </div>
        </div>

        {isLoading && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}