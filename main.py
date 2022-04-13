# modelA : BiLSTM
# modelB : Bert (Classification)
# modelC : Regression(Light BGM)
# Gmodel : BERT Q/A

from app import app, socketio

if __name__ == "__main__":
    socketio.run(app, debug=True, port=6060)
