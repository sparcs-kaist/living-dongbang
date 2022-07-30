const formatTime = (time) => {
    if(time < 10) return "0" + time;
    else return time;
}

const currentTime = (today) => {
    const date = today.getFullYear() + '.' + formatTime(today.getMonth()+1) + '.' + formatTime(today.getDate());
    const time = formatTime(today.getHours()) + ":" + formatTime(today.getMinutes());
    return { date, time };
}

export default currentTime;
