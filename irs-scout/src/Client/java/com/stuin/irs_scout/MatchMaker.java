package com.stuin.irs_scout;

import android.view.View;
import android.widget.TextView;
import com.google.gson.Gson;
import com.stuin.irs_scout.Data.Match;
import com.stuin.irs_scout.Data.Measure;
import com.stuin.irs_scout.Views.Page;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by Stuart on 2/14/2017.
 */
class MatchMaker {
    private Match match = new Match();
    private List<Measure> data = new ArrayList<>();
    private List<Page> pages;
    private TextView status;

    MatchMaker(List<Page> pages, View view) {
        this.pages = pages;
        status = (TextView) view;
        newMatch();
    }

    void newMatch() {
        class Data extends Next {
            @Override
            public void run(List<String> s) {
                super.run(s);
                match = new Gson().fromJson(s.get(0), Match.class);
                if(!MainActivity.position.contains(match.Alliance)) match = new Gson().fromJson(s.get(1), Match.class);

                class Set extends Next {
                    @Override
                    public void run(List<String> measures) {
                        super.run(measures);
                        Gson gson = new Gson();
                        for(String s : measures) data.add(gson.fromJson(s, Measure.class));
                        setMatch();
                    }
                }
                new Request("/matchteam?team=" + getTeam(),new Set());
            }
        }
        new Request("/match", new Data());
    }

    private void setMatch() {
        for(Page p : pages) {
            Map<String, Measure> pageData = new HashMap<>();
            for(Measure m : data) if(m.Page.equals(p.name)) pageData.put(m.Task, m);
            p.setMeasures(pageData, match.Number, getTeam());
        }

        status.setText("Match: " + match.Number + " Team " + MainActivity.position + ": " + getTeam());
    }

    int getTeam() {
        String position = MainActivity.position;
        switch(position.charAt(position.length() - 1)) {
            case '1':
                return match.Team1;
            case '2':
                return match.Team2;
            case '3':
                return match.Team3;
        }
        return 0;
    }
}
