from plagiarismchecker.algorithm import ConsineSim
from apiclient.discovery import build

# searchEngine_API = 'AIzaSyAoEYif8sqEYvj1P6vYLw6CGMrQbDMmaq8'
# searchEngine_API = 'AIzaSyCUYy9AtdMUddiNA0gOcsGPQcE372ytyCw'
# searchEngine_API = 'AIzaSyAQYLRBBeDQNxADPQtUnApntz78-urWEZI'
searchEngine_API = 'AIzaSyCAeR7_6TTKzoJmSwmOuHZvKcVg_lhqvCc'
searchEngine_Id = '758ad3e78879f0e08'

def searchWeb(text, output, c):
    text = text
    # print(text)
    try:
        resource = build("customsearch", 'v1',
                         developerKey=searchEngine_API).cse()
        result = resource.list(q=text, cx=searchEngine_Id).execute()
        searchInfo = result['searchInformation']
        # print(searchInfo)
        if(int(searchInfo['totalResults']) > 0):
            maxSim = 0
            itemLink = ''
            numList = len(result['items']) 
            if numList >= 5:
                numList = 5
            for i in range(0, numList):
                item = result['items'][i]
                content = item['snippet']
                simValue = ConsineSim.cosineSim(text, content)
                if simValue > maxSim:
                    maxSim = simValue
                    itemLink = item['link']
                if item['link'] in output:
                    itemLink = item['link']
                    break
            if itemLink in output:
                print('if', maxSim)
                output[itemLink] = output[itemLink] + 1
                c[itemLink] = ((c[itemLink] *
                                (output[itemLink]-1) + maxSim)/(output[itemLink]))
            else:
                print('else', maxSim)
                print(text)
                print(itemLink)
                output[itemLink] = 1
                c[itemLink] = maxSim
    except Exception as e:
        print(text)
        print(e)
        print('error')
        return output, c, 1
    return output, c, 0
