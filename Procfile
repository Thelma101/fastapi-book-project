# web: ./build.sh && nginx && uvicorn main:app --host 0.0.0.0 --port=${PORT}
# web: nginx -g 'daemon off;' && uvicorn main:app --host 0.0.0.0 --port=${PORT}
web: nginx -g 'daemon off;' & uvicorn main:app --host 0.0.0.0 --port=${PORT}