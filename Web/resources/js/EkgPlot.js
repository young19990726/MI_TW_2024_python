//  Flask 傳到前端的 EKG 數據
const ekgData = JSON.parse(ekgDatastr);

// 設置 SVG 的寬與高
const width = 800;
const height = 200;
const margin = {top: 20, right: 0, bottom: 20, left: 60};
const innerWidth = width - margin.left - margin.right;
const innerHeight = height - margin.top - margin.bottom;

// 設定SVG丟到id為#charts-container的div
const container = d3.select("#charts-container");

ekgData.forEach((data, index) => {
    // 加一個新的 SVG
    const svg = container.append("svg")
        .attr("class", "chart")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    // 設定座標比例
    const xScale = d3.scaleLinear()
        .domain([-0.2, 7])
        .range([0, innerWidth]);

    const yScale = d3.scaleLinear()
        .domain([-2.5,2])
        .range([innerHeight, 0]);

    // 定義線
    const line = d3.line()
        .x((d, i) => xScale(i * 0.001)) // 假設資料點間隔為 0.001 秒
        .y(d => yScale(d));

    // 畫背景格線
    const gridGroup = svg.append("g").attr("class", "grid");

    // X軸格線
    const xGridStepMinor = xScale(0.04) - xScale(0); // 刻度間隔
    for (let x = xScale(-0.2); x <= xScale(7); x += xGridStepMinor) {
        gridGroup.append("line")
            .attr("x1", x)
            .attr("y1", 0)
            .attr("x2", x)
            .attr("y2", innerHeight)
            .attr("stroke", "#FFC0CB") // 格線的顏色
            .attr("stroke-width", 1);
    }

    // Y軸格線
    const yGridStepMinor = yScale(0) - yScale(0.1)  ; // 刻度間隔
    for (let y = 0; y <= innerHeight; y += yGridStepMinor) {
        gridGroup.append("line")
            .attr("x1", 0)
            .attr("y1", y)
            .attr("x2", innerWidth)
            .attr("y2", y)
            .attr("stroke", "#FFC0CB") // 格線的顏色
            .attr("stroke-width", 1);
    }

    // 繪製刻度
    const xAxis = d3.axisBottom(xScale)
        .ticks(36)
        .tickSize(-innerHeight) // 刻度線長度
        .tickFormat(d => d >= -1 && d <= 7 ? d.toFixed(1) : "") // 只在 -0.2-7 範圍内顯示刻度
        .tickValues(d3.range(-0.2, 7, 0.2)); // 設置主刻度為 0.2

    const yAxis = d3.axisLeft(yScale)
        .ticks(10)
        .tickSize(-innerWidth) // 刻度線長度
        .tickFormat(d => d.toFixed(1)); // 格式化刻度標籤

    svg.append("g")
        .attr("transform", `translate(0,${innerHeight})`)
        .call(xAxis)
        .attr("class", "x-axis")
        .append("text")
        .attr("class", "x-axis-label")
        .attr("x", innerWidth / 2)
        .attr("y", margin.bottom+10)
        .attr("text-anchor", "middle")
        .style("font-size", "14px")
        .style("fill", "#000")
        .text("s(秒)");

    svg.append("g")
        .call(yAxis)
        .attr("class", "y-axis")
        .append("text")
        .attr("class", "y-axis-label")
        .attr("x", -margin.left-40)
        .attr("y", innerHeight/2 -120)
        .attr("text-anchor", "middle")
        .attr("transform", "rotate(-90)")
        .style("font-size", "14px")
        .style("fill", "#000")
        .text("mV");

    // y=0 的紅色水平線
    svg.append("line")
        .attr("x1", 0)
        .attr("y1", yScale(0))
        .attr("x2", innerWidth)
        .attr("y2", yScale(0))
        .attr("stroke", "red")
        .attr("stroke-width", 1.5);

    // 繪製 ECG 數據
    svg.append("path")
        .data([data.data])
        .attr("class", "line")
        .attr("d", line)
        .attr("fill", "none")
        .attr("stroke", "#003366")
        .attr("stroke-width", 0.5);


});