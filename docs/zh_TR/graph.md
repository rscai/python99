# Graphs

>**A preliminary remark: The vocabulary in graph theory varies considerably. Some authors use the same word with different meanings. Some authors use different words to mean the same thing. I hope that our definitions are free of contradictions.**
>
>**圖被定義為節點的集合和邊的集合，其中每一條邊都是由一對節點組成。**

```plantuml
graph g {
    g -- h
    b -- c -- f -- b
    f -- k
    d
}
```

>在Python中，有多種方式表示圖。
>
>一個方法是將每一條邊分別表示成一句條文「clause」。按這種方式，圖被描述成：

```python
[(h,g), (k,f), (f,b), ...]
```

>我們稱之為**邊條文形式「edge-clause form」**。
>
>顯然地，孤立的節點不能被表示出來。另一種方法是將整張圖表示成一個數據對象。根據圖的定義是一對集合（節點的和邊的），我們可以使用以下Python數據結構表上述圖例：

```python
([b, c, d, g, h, k], [(b,c), (b, f), (c, f), (f, k), (g, h)])
```

>我們稱之為**圖項「graph-term form」**。謹記，雖然這些列表都是有序的，但它們都是集合，不包含重復的元素。每一條邊只在邊列表𥚃出現一次；比如，一條從節點`x`到節點`y`的邊被表示為`(x, y)`，邊`(y, x)`是不會出現的。**graph-term form是我們的默認形式**。
>
>第三種表現方法關聯節點及相鄰節點集合。我們稱之為**相鄰列表形式「adjacency-kist form」**。例如：

```python
[(b, [c, f]), (c, [b, f]), (d, []), (f, [b, c, k])]
```

>迄今為止，我們所介紹的表現形式都是便於自動處理的，但它們的語法都不用户友好。手寫這些語句是繁瑣及易錯的。我們可以定義一種更緊湊及"人类友好的"的形式：一張圖表示為一個以節點和二元組組成的列表。節點表示孤立節點，二元組表示邊。如果X以邊的端點出現，則其自動被定義為一個節點。我們的例子可以重寫為：

```python
[(b,c), (f, c), (g, h), d, (f, b), (k, f), (h, g)]
```

>我們稱之為**人類友好形式「human-firendly form**。如上所示，列表無需是有序的且有可能包含相同的邊多次。注意孤立的節點`d`。
>
>當邊是有向時我們稱之弧「arcs」。它們以二元組表示。其圖被稱為**有向圖「directed graph」**（或者簡稱digraph）。為了表示有向圖，之前討論的形式需要簡單修改。示例的圖相應地表示為：

```plantuml
digraph d {
    t
    u -> r
    u -> s
    s -> u
    v -> u
}
```

>弧條文形式「Arc-clause form」

```python
[(s, u), (u, r), ...]
```

>圖項形式「Graph-term form」

```python
([r, s, t, u, v], [(s, r), (s, u), (u, r), (u, s), (v, u)])
```

>相鄰列表形式「Adjacency-list form」

```python
[(r, []), (s, [r, u]), (t, []), (u, [r]), (v, [u])]
```

>謹記，相郼列表形式無法區分無向圖和有向圖。

>人類友好形式「Human-friendly form」

```python
[(s, r), t, (u, r), (s, u), (u, s), (v, u)]
```

>最後，無向圖和有向圖可能附加信息至節點和邊（弧）。對節點，沒有問題，只需簡單地用二元組替換單一字符。另一方面，對於邊則需要擴展我們的符法。在邊上包有附加信息的圖被稱為**標記圖「labeled graphs」**。

```plantuml
digraph d {
    p -> m [label=5]
    p -> q [label=9]
    m -> q [label=7]
    k
}
```

>弧條文形式「Arc-clause form」

```python
[(m, q, 7), (p, q, 9), (p, m, 5)]
```

>圖項形式「Graph-term form」

```python
([k, m, p, q], [(m, p, 7), (p, m, 5), (p, q, 9)])
```

>相鄰列表形式「Adjacency-list form」

```python
[(k, []), (m, [(q, 7)]), (p, [(m, 5), (q, 9)]), (q, [])]
```

>注意，邊信息被打包進二元組了。

>人類友好形式「Human-friendly form」

```python
[(p, q, 9], (m, q, 7), k, (p, m, 5)]
```

>標記圖的符號可以用於多重圖「multi-graphs」，其允許在兩點之間存在多條邊（或弧）。
