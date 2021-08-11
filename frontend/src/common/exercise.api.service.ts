import ApiService from "@/common/api.service";
import Exercise from "@/models/exercise.model";
import Player from "@/models/player.model";

class _ExerciseApiService {
  _apiService: typeof ApiService;

  constructor(api: typeof ApiService) {
    this._apiService = api;
  }

  getGames(): Promise<Exercise[]> {
    return this._apiService.get<Exercise[]>("/exercises/").then((result) => {
      return result.data;
    });
  }

  getPlayers(): Promise<Player[]> {
    return this._apiService
      .get<Player[]>("/exercises/players")
      .then((result) => {
        return result.data;
      });
  }
}

const ExerciseApiService = new _ExerciseApiService(ApiService);

export default ExerciseApiService;
