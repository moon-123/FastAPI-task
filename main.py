# pip install python-multipart

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# 파일을 byte단위로 받음. 메모리에 저장됨
# @app.post("/files")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}

@app.post("/files")
async def create_file(file: bytes | None = File(default=None)):
    if not file:
        return {"message": "파일이 존재하지 않음"}
    else:
        return {"file_size": len(file)}

# File()을 따로 생성할 필요가 없음
# 만약 파일의 크기가 메모리 사이즈 이상을 넘어가면 디스크에 저장 => 장점? 단점?
# 이미지, 비디오, 큰 바이너리 파일 등과 같은 파일에 적합
# 메타데이터 정보도 해당 구문을 통해 얻을 수 있음 => 여러가지 장점이 있으니 이 방법이 좋을 것 같다.
@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    if not file:
        return {"message": "파일이 존재하지 않음"}
    else:
        f = open("file.png", "wb")
        f.write(await file.read())
        # print(type(file.read())) # coroutine이 뭘까요?
        # f.write(file.file.read())
        f.close

        return {"file_name": file.filename}
    

# 파일이 없을수도 있으니 -> optional 처리