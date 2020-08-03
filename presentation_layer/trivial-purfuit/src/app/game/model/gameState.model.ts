export interface GameState {
    session_id: string,
    state: {
        available_next_squares?: string,
        current_player: {
            collected_wedges: any[],
            color: string,
            location: number[][],
            player_name: string,
            winning_condition: boolean
        }
    },
    current_round: number,
    current_state: string,
    current_trivia_question?: string,
    moves_left: number,
    players: {
        collected_wedges: any[],
        color: string,
        location: number[][],
        player_name: string,
        winning_condition: boolean 
    }[]
}