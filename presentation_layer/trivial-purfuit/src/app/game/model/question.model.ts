export interface QuestionApiResponse {
    id: string,
    category_id: string,
    correct_answer: string,
    question: string
    possible_answers: string[]
}