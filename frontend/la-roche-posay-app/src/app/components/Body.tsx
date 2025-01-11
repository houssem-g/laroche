"use client"

import React, { useState } from 'react'

interface QAResponse {
  response: string
}

const Body: React.FC = () => {
  const [userQuery, setUserQuery] = useState<string>('')
  const [response, setResponse] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(false)
  const [error, setError] = useState<string | null>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResponse('')

    try {
      const res = await fetch(`http://localhost:8000/qa/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_query: userQuery }),
      })

      if (!res.ok) {
        const errorData = await res.json()
        throw new Error(errorData.detail || 'Quelque chose s\'est mal passé')
      }

      const data: QAResponse = await res.json()
      setResponse(data.response["content"])
    } catch (err: any) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="flex-grow bg-la-roche-posay-gray p-4">
      <div className="max-w-2xl mx-auto bg-la-roche-posay-white p-6 rounded shadow-md">
        <h2 className="text-xl font-semibold mb-4">Posez votre question</h2>
        <form onSubmit={handleSubmit}>
          <textarea
            className="w-full p-2 border border-la-roche-posay-blue rounded mb-4 focus:outline-none focus:ring-2 focus:ring-la-roche-posay-blue"
            rows={4}
            placeholder="Entrez votre question ici..."
            value={userQuery}
            onChange={(e) => setUserQuery(e.target.value)}
            required
          ></textarea>
          <button
            type="submit"
            className="w-full bg-la-roche-posay-blue text-la-roche-posay-white py-2 px-4 rounded hover:bg-la-roche-posay-dark-blue transition duration-200 disabled:opacity-50"
            disabled={loading}
          >
            {loading ? 'Envoi...' : 'Envoyer'}
          </button>
        </form>
        {error && (
          <div className="mt-4 p-2 bg-red-200 text-red-800 rounded">
            {error}
          </div>
        )}
        {response && (
          <div className="mt-4 p-4 bg-la-roche-posay-gray text-la-roche-posay-blue rounded">
            <h3 className="text-lg font-semibold mb-2">Résultat :</h3>
            <p>{response}</p>
          </div>
        )}
      </div>
    </main>
  )
}

export default Body
