import axios, { AxiosError } from 'axios'

const BASE_URL = process.env.NEXT_PUBLIC_API_URL

const baseFetcher = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export function isAxiosError(error: unknown): error is AxiosError {
  return axios.isAxiosError(error)
}

export default baseFetcher
