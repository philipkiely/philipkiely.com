const { OPENAI_API_KEY } = process.env;

exports.handler = async function (event, context) {
    if (event.httpMethod !== 'POST') {
        return { statusCode: 405, body: 'Method Not Allowed' };
    }
    var data = JSON.parse(event.body);
    const res = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + OPENAI_API_KEY,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'model': 'gpt-3.5-turbo',
            'messages': [
                {
                    'role': 'user',
                    'content': 'Write a Shakespearian sonnet that is 14 lines of iambic pentameter with an ABABCDCDEFEFGG rhyme scheme. The subject is ' + data.topic
                }
            ]
        })
    });

    const json = await res.json();
    console.log(json.choices[0].message)
    return {
        statusCode: 200,
        body: json.choices[0].message.content
    }
}

