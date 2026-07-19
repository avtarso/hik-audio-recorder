# hik-audio-recorder

## Цель проекта

Автоматическая запись аудио с RTSP камеры:
- получение аудиопотока;
- анализ сигнала;
- обнаружение событий;
- сохранение интересных фрагментов WAV.

---

## Архитектура

RTSP
 |
 v
RtspAudioSource
 |
 v
AudioFrame
 |
 +----------------+
 |                |
 v                v
CsvRecorder       RecordingSession
                  |
                  v
             AnalysisPipeline
                  |
                  v
             Recorder
                  |
                  v
             WaveWriter

---

## Основные принципы

- компоненты имеют одну ответственность;
- DSP не знает о записи;
- запись не знает о RTSP;
- координаторы не содержат алгоритмов;
- все важные контракты покрыты тестами.

---

## Текущее состояние

Работает:

- RtspAudioSource
- декодирование PyAV
- преобразование AVFrame → AudioFrame
- AnalysisPipeline
- RecordingSession
- WaveWriter
- CsvRecorder
- apps/detect.py

Тесты:
41 passed

---

## Следующий этап

Проверить реальную работу детектора:

RTSP камера
↓
AnalysisPipeline
↓
Event.START
↓
RecordingSession
↓
event_000001.wav

Дальше:
- настройка порогов;
- длительность события;
- pre-buffer;
- post-buffer;
- устойчивость к шуму.