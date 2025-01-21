import plotly.express as px
import plotly.graph_objects as go
from Mapping import create_map



def create_pie_chart(dataframe, mapping):
    label_mapping = create_map(mapping)

    dataset = dataframe.value_counts()

    value, index = dataset.values, dataset.index

    custom_label = index.map(label_mapping)


    fig = go.Figure(data=[go.Pie(
        labels=custom_label,
        values=value,
        textposition='inside',
        textinfo='percent',
        hoverinfo='label+value',
        marker=dict(colors = px.colors.sequential.Darkmint),
        hole=0.3,
        direction='clockwise',
    )])

    fig.update_layout(
        title_x = 0.5,
        title_y = 0.9,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0),
        width=300,
        height=300,
        showlegend=False,
    )

    # fig = px.pie(dataframe, values=value, names=custom_label, color_discrete_sequence=px.colors.sequential.Viridis)
    #
    # fig.update_layout(
    #     title_x = 0.5,
    #     title_y = 0.9
    # )
    #
    #
    #
    # fig.update_layout(
    #     paper_bgcolor='rgba(0,0,0,0)',
    #     plot_bgcolor='rgba(0,0,0,0)',
    #     margin=dict(l=0, r=0, t=0, b=0)
    # )
    #
    # fig.update_layout(showlegend=False)
    #
    # fig.update_traces(textposition='inside', textinfo='percent', hoverinfo='label+value')
    #
    # fig.update_layout(width=300, height=300)
    #
    # fig.update_xaxes(tickangle=-90)

    return fig






